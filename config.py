import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    API_URL = os.environ.get("API_URL")
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
