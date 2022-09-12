from create_connection import start_connection

def start(cursor, conn):
    create_team_table(cursor, conn)
    # create_match_table(cursor, conn)
    conn.close()
    print("Connection closed")

# def create_match_table(cursor, conn):
#     cursor.execute("DROP TABLE IF EXISTS Match")
#     sqlQuery = "CREATE TABLE Match (match_id serial PRIMARY KEY, team_A VARCHAR(255) NOT NULL, team_B VARCHAR(255) NOT NULL, score_A integer NOT NULL, score_B integer NOT NULL)"
#     cursor.execute(sqlQuery)

#     print("Match table created successfully")
#     conn.commit()

def create_team_table(cursor, conn):
    cursor.execute("DROP TABLE IF EXISTS Team")
    sqlQuery = "CREATE TABLE Team (team_id serial PRIMARY KEY, team_name VARCHAR(255) UNIQUE NOT NULL, registration_date DATE NOT NULL, group_id integer NOT NULL, score INTEGER DEFAULT 0, alt_score INTEGER DEFAULT 0, num_goals INTEGER DEFAULT 0, win INTEGER DEFAULT 0, lose INTEGER DEFAULT 0, draw INTEGER DEFAULT 0)"
    cursor.execute(sqlQuery)

    print("Team table created successfully")
    conn.commit()

