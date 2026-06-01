import os
import mysql.connector

DB_CONFIG = {
    "host":     os.environ.get("DB_HOST", "127.0.0.1"),
    "user":     "root",
    "password": "root",
    "database": "news_pipeline"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)