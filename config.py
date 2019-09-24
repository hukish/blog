import os

# This configures our application to behave as required

class Config:
    # Defines the key required by the flask forms
    SECRET_KEY = '1234'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # Defines where the users profile pictures will be stored
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # Defines email configurations that will be used to send emails to the registered users
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    MAIL_PASSWORD

# This defines the configurations during production of the application
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/hudson'
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/hudson'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}