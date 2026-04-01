from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    database_url: str = "sqlite+aiosqlite:///./db/db.sqlite3"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()
