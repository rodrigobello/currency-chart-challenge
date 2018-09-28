import os


class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ENV = 'development'
    # CURRENCY_LAYER_KEY = 'apikey'
    # SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    SECRET = os.environ.get('SECRET')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
