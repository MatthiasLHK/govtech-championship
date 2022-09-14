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
        if len(tmp[1]) == 1 or len(tmp[0]) == 1:
            raise Exception("Invalid date format, please use DD/MM")
        try:
            date = datetime.date(2022, int(tmp[1]), int(tmp[0]))
        except:
            errMessage = "Invalid or missing date value provided"
            raise Exception(errMessage)
        if data[2] != "1" or data[2] != "2":
            raise Exception("Invalid group number, can only choose to be either Group 1 or 2!")
        tmpTeam = Team(data[0], date, data[2])
        teams.append(tmpTeam)
    return teams