from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    email_host: str
    email_port: int
    email_user: str
    email_password: str
    db_url: str

    class Config:
        env_file = ".env"

settings = Settings()
