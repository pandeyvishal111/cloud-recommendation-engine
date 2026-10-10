from typing import Any


class DBConnection:
    """Lightweight database wrapper placeholder for PostgreSQL integration."""

    def __init__(self, dsn: str):
        self.dsn = dsn

    def ping(self) -> dict[str, Any]:
        return {"status": "not_connected", "dsn_configured": bool(self.dsn)}
