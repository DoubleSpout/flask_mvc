class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    HOST = "0.0.0.0"
    PORT = 5000
    SECRET_KEY = "12345"

class Production(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    PORT = 6000

class Debug(Config):
    DEBUG = True
    

