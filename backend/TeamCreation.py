from .Models import Team
import datetime

def createTeams(input):
    entries = input.split("\n")
    teams = []
    for entry in entries:
        if entry == "":
            continue
        entry.strip()
        data = entry.split(" ")
        if len(data) != 3:
            raise Exception("Invalid number of arugments for team creation")
        tmp = data[1].strip().split("/")
        try:
            date = datetime.date(2022, int(tmp[1]), int(tmp[0]))
        except:
            errMessage = "Error: Invalid date value provided"
            raise Exception(errMessage)
        tmpTeam = Team(data[0], date, data[2])
        teams.append(tmpTeam)
    return teams