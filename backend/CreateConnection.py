import psycopg2

def start_connection():
    host = "ec2-35-168-122-84.compute-1.amazonaws.com"
    port = 5432
    database = "dfgl32abg1hg0j"
    user = "ogzttonuqvfmmq"
    password = "e32358527339f7990c2436bf2904d1fda0c590808e1ef489e078815079ff216c"

    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    print("Connected to DB")

    return conn