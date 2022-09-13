from .Models import Match

def createMatches(input):
    entries = input.split("\n")
    matches = []
    for entry in entries:
        if entry == "":
            continue
        entry.strip()
        data = entry.split(" ")
        try:
            teamA = data[0]
            teamB = data[1]
            scoreA = data[2]
            scoreB = data[3]
        except:
            raise Exception("Invalid result entry: " + entry)
        if (not scoreA.isnumeric()):
            raise Exception("Invalid score value for team 1")
        if (not scoreB.isnumeric()):
            raise Exception("Invalid score value for team 2")
        matches.append(Match(teamA, teamB, scoreA, scoreB))
        
    return matches