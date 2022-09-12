from backend.create_connection import start_connection
from backend.Models import Team

class TeamRanker:
    def __init__(self, teams, matches):
        self.teams = teams
        self.matches = matches

    def insertToDb(self, team, cursor):
        teamDb = self.getFromDb(team.teamName, cursor)
        team.score += teamDb.score
        team.altScore += teamDb.altScore
        team.goals += teamDb.goals
        team.win += teamDb.win
        team.lose += teamDb.lose
        team.draw += teamDb.draw
        query = f"UPDATE Team SET score = {team.score}, alt_score = {team.altScore}, num_goals = {team.goals}, win = {team.win}, lose = {team.lose}, draw = {team.draw} WHERE team_name = '{team.teamName}'"
        cursor.execute(query)

        
        
    def getFromDb(self, teamName, cursor):
        query = f"SELECT * FROM Team WHERE team_name = '{teamName}'"
        cursor.execute(query)
        data = cursor.fetchall()[0]
        teamDb = Team(data[1:])
        return teamDb
    
    def rankTeams(self):
        conn = start_connection()
        cursor = conn.cursor()
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
        # self.teams = sorted(self.teams, key=lambda x : (x.score, x.goals, x.altScore, x.registeredDate))
        # self.teams = reversed(self.teams)
        # print(self.teams)
        for team in self.teams:
            self.insertToDb(team, cursor)
        conn.commit()
        conn.close()


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