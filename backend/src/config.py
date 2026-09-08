from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = "Braindump Backend"
    PORT: str = "8000"
    HOST: str = "0.0.0.0"
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/braindump_db"
    
    # Groq / LLM
    GROQ_API_KEY: str = ""
    LLM_MODEL: str = "openai/gpt-oss-20b"

    # Load from .env file automatically
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Instantiate a global settings object
settings = Settings()