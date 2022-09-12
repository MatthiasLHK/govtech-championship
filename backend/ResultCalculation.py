class TeamRanker:
    def __init__(self, teams, matches):
        self.teams = teams
        self.matches = matches

    def insertToDb(self, team, cursor):
        self.getFromDb(team.teamName, cursor)
        
        
    def getFromDb(teamName, cursor):
        query = f"SELECT * FROM Team t WHERE t.teamName = '{teamName}'"
        res = cursor.execute(query)
        print(res)
    
    def rankTeams(self):
        for match in self.matches:
            teamAGoals = match.scoreA
            teamBGoals = match.scoreB

            if teamAGoals > teamBGoals:
                self.updateTeam(match.teamA, "Win", teamAGoals)
                self.updateTeam(match.teamB, "Lose", teamBGoals)
            elif teamAGoals < teamBGoals:
                self.updateTeam(match.teamA, "Lose", teamAGoals)
                self.updateTeam(match.teamB, "Win",teamBGoals)
            else:
                # Draw
                self.updateTeam(match.teamA, "Draw", teamAGoals)
                self.updateTeam(match.teamB, "Draw", teamBGoals)
        self.teams = sorted(self.teams, key=lambda x : (x.score, x.goals, x.altScore, x.registeredDate))
        self.teams = reversed(self.teams)
        # print(self.teams)


    def updateTeam(self, target, result, goals):
        isFound = False
        for team in self.teams:
            if team.teamName == target:
                team.addScore(result)
                team.addGoals(int(goals))
                isFound = True
                break
        if (not isFound):
            print("Error: Team name not registered")