
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    ELASTICSEARCH_URL: str
    REDIS_URL: str
    SENDGRID_API_KEY: str
    EMAIL_FROM: str
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()