from backend.CreateConnection import start_connection
from backend.Models import Team

class TeamRanker:
    def __init__(self, matches):
        self.teams = self.getAllTeams()
        self.matches = matches

    def insertToDb(self, cursor):
        queries = ""
        for team in self.teams:
            queries += f"UPDATE Team SET score = {team.score}, alt_score = {team.altScore}, num_goals = {team.goals}, win = {team.win}, lose = {team.lose}, draw = {team.draw} WHERE team_name = '{team.teamName}';\n"
        print(queries.strip())
        cursor.execute(queries.strip())
    
    def getAllTeams(self):
        teams = []
        conn = start_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Team"
        cursor.execute(query)
        data = cursor.fetchall()
        for entry in data:
            tmp = list(entry)
            tmp = tmp[1:]
            team = Team(tmp)
            teams.append(team)
        return teams

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
        self.insertToDb(cursor)
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
            raise Exception("Error: Team name not registered")