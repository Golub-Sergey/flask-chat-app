import os

class Configuration(object):
    MONGO_URI = 'mongodb://localhost:27017/chat'
    SECRET_KEY = str(os.urandom(24))