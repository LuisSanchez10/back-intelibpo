import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = True
    DB_USER = os.getenv('DB_USER')
    DB_CONNECTOR = os.getenv('DB_CONNECTOR')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = 5432
    DB_SCHEMA = os.getenv('DB_SCHEMA')
    SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s:%i/%s' % (
        DB_CONNECTOR,
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_SCHEMA,
    )
