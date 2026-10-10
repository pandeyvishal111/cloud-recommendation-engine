import hashlib
import secrets
import uuid
from typing import Any

from argon2 import PasswordHasher

from app.services.database_service import DatabaseService


_USERS: dict[str, dict[str, Any]] = {}

argon2_hasher = PasswordHasher()


def _hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 200_000)
    return f"pbkdf2_sha256${salt}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    if not stored:
        return False
    if stored.startswith("pbkdf2_sha256$"):
        _, salt, digest_hex = stored.split("$", 2)
        current = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 200_000)
        return current.hex() == digest_hex
    if stored.startswith("$"):
        try:
            return argon2_hasher.verify(stored, password)
        except Exception:
            return False
    return stored == password


class AuthService:
    @staticmethod
    def _ensure_user_table() -> None:
        conn = DatabaseService.get_connection()
        if conn is None:
            return
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS users (
                        id VARCHAR(255) PRIMARY KEY DEFAULT gen_random_uuid()::text,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        full_name VARCHAR(255),
                        company VARCHAR(255),
                        password_hash TEXT NOT NULL,
                        created_at TIMESTAMPTZ DEFAULT NOW()
                    )
                    """
                )
                cur.execute(
                    "SELECT column_name FROM information_schema.columns WHERE table_name = 'users'"
                )
                existing_columns = {row[0] for row in cur.fetchall()}
                if "full_name" not in existing_columns:
                    cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS full_name VARCHAR(255)")
                if "company" not in existing_columns:
                    cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS company VARCHAR(255)")
                if "first_name" not in existing_columns and "last_name" not in existing_columns:
                    cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS first_name VARCHAR(255)")
                    cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS last_name VARCHAR(255)")
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def _row_to_user(row: dict[str, Any]) -> dict[str, Any]:
        full_name = row.get("full_name")
        if not full_name:
            first_name = str(row.get("first_name") or "").strip()
            last_name = str(row.get("last_name") or "").strip()
            full_name = " ".join(part for part in (first_name, last_name) if part)
        return {
            "email": row.get("email"),
            "full_name": full_name or "User",
            "company": row.get("company"),
            "password_hash": row.get("password_hash"),
        }

    @staticmethod
    def _ensure_demo_user() -> None:
        demo_email = "demo@example.com"
        demo_password = "Password123!"
        if demo_email in _USERS:
            return

        _USERS[demo_email] = {
            "email": demo_email,
            "full_name": "Demo User",
            "company": "Contoso",
            "password_hash": _hash_password(demo_password),
        }

        conn = DatabaseService.get_connection()
        if conn is None:
            return
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT column_name FROM information_schema.columns WHERE table_name = 'users'"
                )
                columns = {row[0] for row in cur.fetchall()}
                user_id = str(uuid.uuid4())

                first_name = "Demo"
                last_name = "User"
                full_name = "Demo User"
                company = "Contoso"

                if "first_name" in columns and "last_name" in columns:
                    cur.execute(
                        """
                        INSERT INTO users (id, first_name, last_name, email, password_hash, full_name, company, created_at)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
                        ON CONFLICT (email) DO NOTHING
                        """,
                        (user_id, first_name, last_name, demo_email, _hash_password(demo_password), full_name, company),
                    )
                else:
                    cur.execute(
                        """
                        INSERT INTO users (id, email, full_name, company, password_hash)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (email) DO NOTHING
                        """,
                        (user_id, demo_email, full_name, company, _hash_password(demo_password)),
                    )
            conn.commit()
        except Exception:
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def register_user(email: str, password: str, full_name: str, company: str | None = None) -> dict[str, Any]:
        normalized_email = email.strip().lower()
        if not normalized_email or not password:
            raise ValueError("Email and password are required.")

        if normalized_email in _USERS:
            raise ValueError("User already exists.")

        AuthService._ensure_user_table()

        conn = DatabaseService.get_connection()
        if conn is not None:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users WHERE email = %s", (normalized_email,))
                    if cur.fetchone() is not None:
                        raise ValueError("User already exists.")

                    cur.execute(
                        "SELECT column_name FROM information_schema.columns WHERE table_name = 'users'"
                    )
                    columns = {row[0] for row in cur.fetchall()}
                    password_hash = _hash_password(password)

                    user_id = str(uuid.uuid4())

                    first_name, last_name = (full_name.split(" ", 1) + [""])[:2]
                    if "first_name" in columns and "last_name" in columns:
                        cur.execute(
                            "INSERT INTO users (id, first_name, last_name, email, password_hash, full_name, company, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())",
                            (user_id, first_name, last_name, normalized_email, password_hash, full_name, company),
                        )
                    elif "full_name" in columns and "company" in columns:
                        cur.execute(
                            "INSERT INTO users (id, email, full_name, company, password_hash) VALUES (%s, %s, %s, %s, %s)",
                            (user_id, normalized_email, full_name, company, password_hash),
                        )
                    else:
                        cur.execute(
                            "INSERT INTO users (id, email, password_hash) VALUES (%s, %s, %s)",
                            (user_id, normalized_email, password_hash),
                        )
                conn.commit()
            except Exception as exc:
                conn.rollback()
                raise ValueError(str(exc)) from exc
            finally:
                conn.close()

        _USERS[normalized_email] = {
            "email": normalized_email,
            "full_name": full_name,
            "company": company,
            "password_hash": _hash_password(password),
        }
        return {
            "email": normalized_email,
            "full_name": full_name,
            "company": company,
        }

    @staticmethod
    def authenticate_user(email: str, password: str) -> dict[str, Any] | None:
        normalized_email = email.strip().lower()
        if normalized_email == "demo@example.com" and password == "Password123!":
            AuthService._ensure_demo_user()

        conn = DatabaseService.get_connection()
        if conn is not None:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users WHERE email = %s", (normalized_email,))
                    row = cur.fetchone()
                    if row is not None:
                        columns = [desc[0] for desc in cur.description]
                        user_data = dict(zip(columns, row))
                        stored_user = AuthService._row_to_user(user_data)
                        if verify_password(password, stored_user["password_hash"]):
                            return {
                                "email": stored_user["email"],
                                "full_name": stored_user["full_name"],
                                "company": stored_user["company"],
                            }
                        return None
            finally:
                conn.close()

        user = _USERS.get(normalized_email)
        if user is None:
            return None
        if not verify_password(password, user["password_hash"]):
            return None
        return {
            "email": user["email"],
            "full_name": user["full_name"],
            "company": user["company"],
        }

    @staticmethod
    def list_users() -> list[dict[str, Any]]:
        conn = DatabaseService.get_connection()
        if conn is not None:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users ORDER BY created_at DESC")
                    rows = cur.fetchall()
                    columns = [desc[0] for desc in cur.description]
                return [AuthService._row_to_user(dict(zip(columns, row))) for row in rows]
            finally:
                conn.close()

        return [
            {"email": user["email"], "full_name": user["full_name"], "company": user["company"]}
            for user in _USERS.values()
        ]
