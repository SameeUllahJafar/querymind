from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    """Application settings."""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://querymind:querymind@localhost:5432/querymind"
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-opus-4-8"
    cors_origins: list[str] = ["http://localhost:3000"]

    
settings = Settings()