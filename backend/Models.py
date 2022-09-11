class Team:
    def __init__(self, name, registedDate, groupId):
        self.teamName = name
        self.groupId = groupId
        self.registeredDate = registedDate

    def teamInfo(self):
        info = f"{self.teamName} | {self.registeredDate} | {self.groupId}"
        return info

class Match:
    def __init__(self, teamA, teamB, scoreA, scoreB):
        self.teamA = teamA
        self.teamB = teamB
        self.scoreA = scoreA
        self.scoreB = scoreB
    def matchInfo(self):
        info = f"{self.teamA} | {self.teamB} | {self.scoreA} | {self.scoreB}"
        return info