import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False
    CHARGILY_KEY = os.getenv("CHARGILY_KEY")
    CHARGILY_SECRET = os.getenv("CHARGILY_SECRET")
    ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD", "changeme")
    ELASTIC_HOST = os.getenv("ELASTIC_HOST", "https://localhost:9200")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database_dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database_test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}

key = Config.SECRET_KEY
