import psycopg2
import os

def start_connection():
    host = ""
    port = 0
    database = ""
    user = ""
    password = ""

    try:
        if host == "":
            DATABASE_URL = os.environ['DATABASE_URL']
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        else:
            conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
            print("Connected to DB")
        return conn
    except:
        raise Exception("Failed to connect to database!")

    