import os


class Config(object):
    ENV = os.environ.get("ENV", "DEVELOPMENT")
    CSRF_ENABLED = True
    JWT_SECRET_KEY = "RESURFACE_SECRET"
    SECRET_KEY = "RESURFACE_SECRET"

    # Database Setup
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DefaultConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///hackernews.db"
