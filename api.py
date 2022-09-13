from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
import ast
from backend.TeamCreation import createTeams
from backend.MatchCreation import createMatches
from backend.ResultCalculation import TeamRanker
from backend.CreateConnection import start_connection
from backend.InsertTable import insert_team
from backend.CreateTable import create_team_table


app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/team-creation", methods=["POST"])
@cross_origin()
def makeTeams():
    print("Making teams")
    tmp = request.data.decode("UTF-8")
    data = ast.literal_eval(tmp)
    if data['info'] == "":
        return "0"
    try:
        teams = createTeams(data['info'])
    except Exception as error:
        return error, 400
    conn = start_connection()
    insert_team(teams, conn)
    conn.commit()
    conn.close()
    result = {}
    result['teams'] = str(len(teams))
    tmp = []
    return result

    

@app.route("/submit-results", methods=["POST"])
@cross_origin()
def submitMatchResults():
    tmp = request.data.decode("UTF-8")
    data = ast.literal_eval(tmp)
    if data['info'] == "":
        return "0"
    try:
        matches = createMatches(data['info'])
        rankTeams(matches)
    except Exception as error:
        return error, 400
    return len(matches)

@app.route("/getRankingA", methods=["GET"])
@cross_origin()
def getRankingA():
    conn = start_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Team WHERE group_id = 1 ORDER BY score DESC, num_goals DESC, alt_score DESC, registration_date ASC"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    response = []
    rank = 1
    for entry in data:
        tmp = list(entry)
        tmp[0] = rank
        response.append(tmp)
        rank += 1
    return response

@app.route("/getRankingB", methods=["GET"])
@cross_origin()
def getRankingB():
    conn = start_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Team WHERE group_id = 2 ORDER BY score DESC, num_goals DESC, alt_score DESC, registration_date ASC"
    cursor.execute(query)
    data = cursor.fetchall()
    response = []
    rank = 1
    for entry in data:
        tmp = list(entry)
        tmp[0] = rank
        response.append(tmp)
        rank += 1
    return response

@app.route("/clearData", methods=["GET"])
@cross_origin()
def clearAllData():
    print("Clearing data")
    conn = start_connection()
    cursor = conn.cursor()
    create_team_table(cursor, conn)
    return "Data cleared!"

def rankTeams(matches):
    ranker = TeamRanker(matches)
    ranker.rankTeams()
