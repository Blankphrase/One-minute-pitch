import os


class Config:
    '''
    general configuration
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blankphrase:password@localhost/pitch'

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
