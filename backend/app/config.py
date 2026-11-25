from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration lue depuis les variables d'environnement (voir .env.example)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    database_url: str = "postgresql+psycopg://passage:passage@localhost:5432/passage"
    secret_key: str = ""
    timezone: str = "Africa/Douala"
    # Vide = mode sans clé : la synthèse utilise le gabarit déterministe.
    ai_api_key: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
