import os


class Config:
    '''
    general configuration
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blankphrase:password@localhost/pitch'

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    
class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
