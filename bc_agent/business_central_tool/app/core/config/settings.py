from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# ============================================================
# PROJECT ROOT
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[6]
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    """
    Central application configuration.

    Values are loaded from environment variables and .env.
    """

    # ========================================================
    # Azure / Foundry
    # ========================================================

    foundry_project_endpoint: str | None = None
    azure_ai_endpoint: str | None = None
    azure_ai_key: str | None = None
    azure_openai_deployment: str | None = None
    azure_openai_api_version: str | None = None

    azure_tenant_id: str | None = None
    azure_client_id: str | None = None
    azure_client_secret: str | None = None

    # ========================================================
    # Business Central
    # ========================================================

    bc_tenant_id: str
    bc_client_id: str
    bc_client_secret: str

    bc_base_url: str = (
        "https://api.businesscentral.dynamics.com"
    )

    bc_environment: str = "Production"

    bc_api_version: str = "v2.0"

    bc_company_id: str

    # ========================================================
    # HTTP
    # ========================================================

    http_timeout: float = 120.0

    # ========================================================
    # Retry
    # ========================================================

    max_retries: int = 3
    max_retry_delay: int = 10

    # ========================================================
    # Token
    # ========================================================

    token_refresh_buffer: int = 300

    # ========================================================
    # Logging
    # ========================================================

    log_level: str = "INFO"

    # ========================================================
    # Pydantic configuration
    # ========================================================

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()