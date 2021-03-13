import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ENV = os.environ.get("ENV", "DEVELOPMENT")
    CSRF_ENABLED = True
    JWT_SECRET_KEY = "RESURFACE_SECRET"
    SECRET_KEY = "RESURFACE_SECRET"

    # Database Setup
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DefaultConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "hackernews.db")
