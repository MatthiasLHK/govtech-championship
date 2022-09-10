from flask import Flask, request
import ast
from models.TeamCreation import createTeams
app = Flask(__name__)

@app.route("/team-creation", methods=["POST"])
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
def submitMatchResults():
    return "Match results"