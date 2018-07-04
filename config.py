"""
Application configuration settings
"""
import os

class Config:
    """
    Common configurations
    """ 
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    DBNAME = "ride_my_way"
    DBUSER = "zawi"
    DBPASSWORD = "password"

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}