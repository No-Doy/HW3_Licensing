import os

# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = 'secretkeyguys'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #print SQLALCHEMY_DATABASE_URI

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

SECRET_KEY = 'secretkeyguys'
WTF_CSRF_ENABLED = True