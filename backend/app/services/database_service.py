from __future__ import annotations

import json
from typing import Any

import psycopg2
from psycopg2.extras import RealDictCursor

from app.config import settings


class DatabaseService:
    @staticmethod
    def get_connection():
        try:
            return psycopg2.connect(settings.DB_DSN, sslmode="require")
        except Exception:
            return None

    @staticmethod
    def ensure_schema() -> bool:
        conn = DatabaseService.get_connection()
        if conn is None:
            return False

        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS saved_searches (
                        id SERIAL PRIMARY KEY,
                        user_email VARCHAR(255) NOT NULL,
                        title VARCHAR(255) NOT NULL,
                        payload JSONB NOT NULL,
                        created_at TIMESTAMPTZ DEFAULT NOW()
                    )
                    """
                )
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def save_search(user_email: str, title: str, payload: dict[str, Any]) -> dict[str, Any]:
        if not DatabaseService.ensure_schema():
            return {
                "status": "error",
                "message": "Live PostgreSQL storage is not configured or unavailable.",
            }

        conn = DatabaseService.get_connection()
        if conn is None:
            return {
                "status": "error",
                "message": "Live PostgreSQL connection unavailable.",
            }

        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "INSERT INTO saved_searches (user_email, title, payload) VALUES (%s, %s, %s) RETURNING id, created_at",
                    (user_email, title, json.dumps(payload)),
                )
                row = cur.fetchone()
            conn.commit()
            return {
                "status": "saved",
                "id": row["id"],
                "created_at": str(row["created_at"]),
            }
        except Exception as exc:
            conn.rollback()
            return {"status": "error", "message": str(exc)}
        finally:
            conn.close()

    @staticmethod
    def list_searches(user_email: str | None = None) -> list[dict[str, Any]]:
        conn = DatabaseService.get_connection()
        if conn is None:
            return []

        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                if user_email:
                    cur.execute(
                        "SELECT id, title, payload, created_at FROM saved_searches WHERE user_email = %s ORDER BY created_at DESC",
                        (user_email,),
                    )
                else:
                    cur.execute(
                        "SELECT id, title, payload, created_at FROM saved_searches ORDER BY created_at DESC"
                    )
                rows = cur.fetchall()
            return [
                {
                    "id": row["id"],
                    "title": row["title"],
                    "payload": row["payload"],
                    "created_at": str(row["created_at"]),
                    "status": "saved",
                }
                for row in rows
            ]
        except Exception:
            return []
        finally:
            conn.close()
