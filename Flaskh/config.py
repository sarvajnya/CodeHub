import os


class Config_info(object):
    SECRETKEY = os.urandom(32)
    SECRET_KY = os.environ.get('SECRET_KEY') or SECRETKEY

    MONGODB_SETTINGS = {'db': 'Compiler'}
