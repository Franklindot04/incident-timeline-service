from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_path: str = "incidents.db"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
