# encodeing: utf-8

import os

DEBUG = True

SECRET_KEY = os.urandom(24)

# HOSTNAME = '127.0.0.1'
# PORT     = '3306'
# DATABASE = 'flsk_mall'
# USERNAME = 'root'
# PASSWORD = 'root'
# DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8', format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# SQLALCHEMY_DATABASE_URI = DB_URI

APP_ITEM = [
    'polls.apps',
]

COMMAND_TIME = [
    'polls',
]