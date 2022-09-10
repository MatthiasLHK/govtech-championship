from models.Models import Team

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
        tmpTeam = Team(data[0], data[1], data[2])
        teams.append(tmpTeam)
    # print("Completed")
    # print(teams)
    return teams