from pydantic_settings import BaseSettings, SettingsConfigDict

class Data(BaseSettings):
    URL: str
    API_KEY: str
    model_config = SettingsConfigDict(env_file=".env")