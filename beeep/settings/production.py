from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "bleep1.herokuapp.com "
]
django_heroku.settings(locals())