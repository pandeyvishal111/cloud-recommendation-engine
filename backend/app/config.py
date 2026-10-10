import os
from pathlib import Path
from typing import Optional

ROOT_DIR = Path(__file__).resolve().parents[2]
_ENV_OVERRIDES: dict[str, str] = {}


def _normalize_env_key(key: str) -> str:
    return key.strip().replace("-", "_").replace(" ", "_").upper()


def _key_candidates(key: str) -> list[str]:
    raw = key.strip()
    variants = {
        raw,
        raw.upper(),
        raw.lower(),
        raw.replace("-", "_"),
        raw.replace("-", "_" ).upper(),
        raw.replace(" ", "_"),
        raw.replace(" ", "_").upper(),
        raw.replace(" ", "").replace("-", "_"),
        raw.replace(" ", "").replace("-", "_").upper(),
        raw.replace(" ", "").replace("-", ""),
        raw.replace(" ", "").replace("-", "").upper(),
        raw.replace(" ", "_").replace("-", "") ,
        raw.replace(" ", "_").replace("-", "").upper(),
        _normalize_env_key(raw),
        _normalize_env_key(raw).replace("_", ""),
    }
    return [value for value in variants if value]


def _load_env_file_fallback(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return

    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key_part, value_part = line.split("=", 1)
        key = key_part.strip()
        value = value_part.strip().strip('"').strip("'")
        if not key:
            continue

        for alias in _key_candidates(key):
            _ENV_OVERRIDES.setdefault(alias, value)
            os.environ.setdefault(alias, value)


_load_env_file_fallback(ROOT_DIR / ".env")


def getenv_first(*keys: str) -> Optional[str]:
    seen = set()
    for key in keys:
        if key in seen:
            continue
        seen.add(key)

        for candidate in _key_candidates(key):
            value = _ENV_OVERRIDES.get(candidate)
            if value is None:
                value = os.getenv(candidate)
            if value is not None and str(value).strip() != "":
                return str(value).strip().strip('"').strip("'")

        direct = os.getenv(key)
        if direct is not None and str(direct).strip() != "":
            return str(direct).strip().strip('"').strip("'")
    return None


def parse_blob_account_key(raw: str) -> Optional[str]:
    if not raw:
        return None
    for part in raw.split(";"):
        if part.startswith("AccountKey="):
            return part.split("=", 1)[1]
    return None


def parse_azure_deployment(raw: str) -> Optional[str]:
    if not raw:
        return None
    if "/" in raw:
        return raw.split("/")[-1].strip()
    return raw.strip()


class Settings:
    APP_NAME = "Cloud Recommendation Engine"
    SECRET_KEY = getenv_first("SECRET_KEY", "JWT_SECRET", "dev-secret-key")

    DB_DSN = getenv_first(
        "DBConnectionstring",
        "POSTGRES_DSN",
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/cloud_reco"
    )

    AZURE_OPENAI_ENDPOINT = getenv_first("Endpoint", "AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = getenv_first("API key", "APIKEY", "AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_DEPLOYMENT = parse_azure_deployment(
        getenv_first("Azure OpenAI", "AZURE_OPENAI_DEPLOYMENT")
    )
    AZURE_OPENAI_MODEL = getenv_first("Model", "AZURE_OPENAI_MODEL")
    AZURE_OPENAI_API_VERSION = getenv_first("API version", "AZURE_OPENAI_API_VERSION", "2025-04-01-preview")

    BLOB_ACCOUNT_NAME = getenv_first("BlobstorageName", "AZURE_STORAGE_ACCOUNT_NAME")
    BLOB_ACCOUNT_KEY = parse_blob_account_key(
        getenv_first("DefaultEndpointsProtocol", "AZURE_STORAGE_CONNECTION_STRING", "")
    ) or getenv_first("AZURE_STORAGE_ACCOUNT_KEY")

    if BLOB_ACCOUNT_NAME and BLOB_ACCOUNT_KEY:
        AZURE_STORAGE_CONNECTION_STRING = (
            f"DefaultEndpointsProtocol=https;AccountName={BLOB_ACCOUNT_NAME};"
            f"AccountKey={BLOB_ACCOUNT_KEY};EndpointSuffix=core.windows.net"
        )
    else:
        AZURE_STORAGE_CONNECTION_STRING = getenv_first(
            "AZURE_STORAGE_CONNECTION_STRING",
            "BlobStorageConnectionString",
            "UseDevelopmentStorage=true"
        )


settings = Settings()
