from .Models import Match

def createMatches(input):
    entries = input.split("\n")
    matches = []
    for entry in entries:
        if entry == "":
            continue
        entry.strip()
        data = entry.split(" ")
        matches.append(Match(data[0], data[1], data[2], data[3]))
    return matches