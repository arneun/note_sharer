import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nobody likes you'
    USER_NAME = 'Maniek'


