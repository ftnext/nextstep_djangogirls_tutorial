import os

from dotenv import load_dotenv

from .base import *  # NOQA


load_dotenv()

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')
