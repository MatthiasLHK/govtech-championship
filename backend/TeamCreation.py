from .Models import Team
import datetime

def createTeams(input):
    # print(input)
    entries = input.split("\n")
    # print(entries)
    teams = []
    for entry in entries:
        if entry == "":
            continue
        entry.strip()
        data = entry.split(" ")
        tmp = data[1].strip().split("/")
        date = datetime.date(2022, int(tmp[1]), int(tmp[0]))
        # print(date)
        tmpTeam = Team(data[0], date, data[2])
        teams.append(tmpTeam)
    return teams