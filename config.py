class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    PWD_HASH_ITERATIONS = 100000

    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {"ensure_ascii": False, "indent": 3, "sort_keys": False}



