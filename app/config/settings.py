from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ELASTICSEARCH_URL: str
    REDIS_URL: str

    class Config:
        env_file = ".env"

settings = Settings()