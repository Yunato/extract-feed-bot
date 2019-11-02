import psycopg2
import urllib.parse as urlparse
import os

def get_connection():
    url = os.environ.get('DATABASE_URL')
    return psycopg2.connect(url)

