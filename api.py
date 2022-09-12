from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
import ast
from backend.TeamCreation import createTeams
from backend.MatchCreation import createMatches
from backend.ResultCalculation import TeamRanker
from backend.create_connection import start_connection
from backend.insert_table import insert_team


app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

tmpCache = {}

@app.route("/team-creation", methods=["POST"])
@cross_origin()
def makeTeams():
    tmp = request.data.decode("UTF-8")
    data = ast.literal_eval(tmp)
    if data['info'] == "":
        return "0"
    teams = createTeams(data['info'])
    tmpCache['teams'] = teams
    conn = start_connection()
    insert_team(teams, conn)
    conn.commit()
    conn.close()
    result = {}
    result['teams'] = str(len(teams))
    tmp = []
    # for team in teams:
    #     tmp.append(team.teamInfo())
    # result["teamsInfo"] = tmp
    return result

    

@app.route("/submit-results", methods=["POST"])
@cross_origin()
def submitMatchResults():
    tmp = request.data.decode("UTF-8")
    data = ast.literal_eval(tmp)
    if data['info'] == "":
        return "0"
    matches = createMatches(data['info'])
    rankTeams(matches)
    result = {}
    result['matches'] = str(len(matches))
    tmp = []
    for match in matches:
        tmp.append(match.matchInfo())
    result["matchInfo"] = tmp
    return result

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

def rankTeams(matches):
    ranker = TeamRanker(tmpCache['teams'], matches)
    ranker.rankTeams()
    teams = ranker.teams
    for team in teams:
        print(team.teamInfo())
