import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN', 'summy-dummy token')

DATABASE = 'YaNotes.sqlite3'
