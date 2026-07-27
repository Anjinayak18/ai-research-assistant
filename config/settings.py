from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Research & Knowledge Assistant"

    APP_VERSION: str = "1.0.0"

    GOOGLE_API_KEY: str = ""

    DATABASE_URL: str = "sqlite:///./data/database/app.db"

    VECTOR_DB_PATH: str = "./data/vector_db"

    UPLOAD_DIR: str = "./data/raw_documents"

    OPENAI_API_KEY: str = ""

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    MODEL_PATH: str = "./models/tf_classifier.h5"

    TOKENIZER_PATH: str = "./models/tokenizer.pickle"

    LABEL_ENCODER_PATH: str = "./models/label_encoder.pkl"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
