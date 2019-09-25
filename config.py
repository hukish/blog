import os

# This configures our application to behave as required

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 
    # Defines the key required by the flask forms
    SECRET_KEY =    '1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/hudson'


    # Defines where the users profile pictures will be stored
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # Defines email configurations that will be used to send emails to the registered users
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "hudsonhukish@gmail.com"
    MAIL_PASSWORD = "NOTEKCS158M"

    def init_app(app):
        pass


# This defines the configurations during production of the application
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 
   
    
    
   
    pass

class DevConfig(Config):
    
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/hudson' 

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}