import os  # allow for interaction with the operating system dependent functionality

class Config:
    """
    Describes the general configurations
    """
    SECRET_KEY ='muema'
    UPLOADED_PHOTOS_DEST= 'app/static/photos'  # storage location of photos
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://joseph:25MuemA25@localhost/blogger'

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # mail configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'pitchymojo@gmail.com'
    MAIL_PASSWORD  = '25MuemA25'
    

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    """
    Describes production configuration child class
    Args:
        Config: The parent configration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://joseph:25MUemA25@localhost/blogger'    

class DevConfig(Config):
    """
    Describes development configuration child class
    Args:
         Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://joseph:25MuemA25@localhost/blogger'
    DEBUG = True

# Dictionary that helps us access the different configuration option classes
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}