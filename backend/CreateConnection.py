import psycopg2

def start_connection():
    host = ""
    port = 0
    database = ""
    user = ""
    password = ""

    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        print("Connected to DB")
        return conn
    except:
        raise Exception("Failed to connect to database!")

    