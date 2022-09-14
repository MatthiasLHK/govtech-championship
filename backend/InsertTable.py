def insert_team(teams, conn):
    cursor = conn.cursor()
    counter = 0
    sqlQuery = "INSERT INTO Team (team_name, registration_date, group_id, score, alt_score, num_goals, win, lose, draw) VALUES "
    for team in teams:
        values = f"('{team.teamName}', '{str(team.registeredDate)}', {team.groupId}, {team.score}, {team.altScore}, {team.goals}, {team.win}, {team.lose}, {team.draw})"
        query = sqlQuery + values
        try:
            cursor.execute(query)
        except:
            raise Exception("This team has already registered: " + team.teamName)
        counter += 1
    print(f"{counter} team has been inserted")
