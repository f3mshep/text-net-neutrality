# -*- coding: utf-8 -*-
from os import path

class Config(object):
    DEBUG = False
    TESTING = False
    ROOT_DIR = path.abspath(
        path.dirname(path.join(__file__))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/test.db' % (ROOT_DIR)
    SECRET_KEY='\x62\x27\x44\x5c\x78\x39\x32\x5c\x78\x31\x37\x5c\x78\x31\x31\x5c\x78\x61\x31\x64\x5c\x78\x63\x33\x5c\x78\x62\x33\x5c\x78\x31\x36\x59\x4b\x5c\x78\x64\x66\x64\x25\x5c\x78\x39\x31\x5c\x78\x38\x37\x56\x4a\x5c\x78\x31\x38\x40\x5c\x78\x38\x66\x3c\x5c\x78\x63\x31\x5c\x78\x63\x33\x27'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/foo'
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_NATIVE_UNICODE = True
