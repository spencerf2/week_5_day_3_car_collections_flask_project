import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Regardless of the operating system
# Allow outside files/folders to be added to the project from the
# Base directory

class Config():
    """
        Use Environment variables unless we specify otherwise.
        Create config variables and use these settings.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:enter_password_here@127.0.0.1:5432/car-collection'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off Update Messages from sqlalchemy
    