import psycopg2

def start_connection():
    host = "ec2-3-213-228-206.compute-1.amazonaws.com"
    port = 5432
    database = "da6rj4ntkdcm9"
    user = "jviiitadnleeyu"
    password = "de43b3de8db5737cca8c012a6e6add7fd299826ea1bd76dd97ba3ab4a53dc0e7"

    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    print("Connected to DB")

    return conn