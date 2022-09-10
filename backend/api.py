from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
import ast
from models.TeamCreation import createTeams

app = Flask(__name__, static_folder='govtech-championship/build', static_url_path='')
CORS(app)

@app.route("/team-creation", methods=["POST"])
@cross_origin()
def makeTeams():
    tmp = request.data.decode("UTF-8")
    data = ast.literal_eval(tmp)
    # print(data['teams'])
    if data['teams'] == "":
        return "0"
    teams = createTeams(data['teams'])
    # print(teams)
    result = {}
    result['teams'] = str(len(teams))
    tmp = []
    for team in teams:
        tmp.append(team.teamInfo())
    result["teamsInfo"] = tmp
    return result

    

@app.route("/submit-results", methods=["POST"])
@cross_origin()
def submitMatchResults():
    return "Match results"
@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')