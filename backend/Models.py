class Team:

    def __init__(self, *args):
        if len(args) == 3:
            self.teamName = args[0]
            self.registeredDate = args[1]
            self.groupId = args[2]
            self.score = 0
            self.altScore = 0
            self.goals = 0
            self.win = 0
            self.lose = 0
            self.draw = 0
        else:
            args = args[0]
            self.teamName = args[0]
            self.registeredDate = args[1]
            self.groupId = args[2]
            self.score = args[3]
            self.altScore = args[4]
            self.goals = args[5]
            self.win = args[6]
            self.lose = args[7]
            self.draw = args[8]

    def teamInfo(self):
        info = f"{self.teamName} | {self.registeredDate} | {self.groupId} | {self.score} | {self.altScore} | {self.goals}"
        return info

    def addScore(self, result):
        if result == "Win":
            self.score += 3
            self.altScore += 5
            self.win += 1
        elif result == "Draw":
            self.score += 1
            self.altScore += 3
            self.draw += 1
        elif result == "Lose":
            self.score += 0
            self.altScore += 1
            self.lose += 1
        else:
            print("Error: Invalid result - " + result)

    def addGoals(self, numOfGoals):
        self.goals += numOfGoals

    def getScores(self):
        return self.score, self.altScore 

class Match:
    def __init__(self, teamA, teamB, scoreA, scoreB):
        self.teamA = teamA
        self.teamB = teamB
        self.scoreA = scoreA
        self.scoreB = scoreB

    def matchInfo(self):
        info = f"{self.teamA} | {self.teamB} | {self.scoreA} | {self.scoreB}"
        return info
    

