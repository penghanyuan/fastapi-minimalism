from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {
        "case_sensitive": True
    }
    PROJECT_NAME: str = "FastAPI Template"
    API_V1_STR: str = "/api/v1"

    MODEL_PATH: str = "app/ml_model/model.pth"


settings = Settings()
