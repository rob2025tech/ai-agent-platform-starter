from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "gemma3:4b"
    # ollama_url: str
    # ollama_model: str

    # class Config:
    #     env_file = ".env"


settings = Settings()