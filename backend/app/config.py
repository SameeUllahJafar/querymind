from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    """Application settings."""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://querymind:querymind@localhost:5432/querymind"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.5-flash"
    cors_origins: list[str] = ["http://localhost:3000"]

    
settings = Settings()