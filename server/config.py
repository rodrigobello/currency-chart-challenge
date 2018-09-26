import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    CURRENCY_LAYER_KEY = 'ADD_CURRENCY_LAYER_KEY'


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SECRET = os.getenv('SECRET')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
