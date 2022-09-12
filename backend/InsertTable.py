def insert_team(teams, conn):
    cursor = conn.cursor()
    counter = 0
    sqlQuery = "INSERT INTO Team (team_name, registration_date, group_id, score, alt_score, num_goals, win, lose, draw) VALUES "
    for team in teams:
        values = f"('{team.teamName}', '{str(team.registeredDate)}', {team.groupId}, {team.score}, {team.altScore}, {team.goals}, {team.win}, {team.lose}, {team.draw}), "
        sqlQuery += values
        counter += 1
    sqlQuery = sqlQuery[:-2]
    cursor.execute(sqlQuery)
    print(f"{counter} team has been inserted")

# def insert_matches(matches, conn):
#     cursor = conn.cursor()
#     counter = 0
#     query = "INSERT INTO Match (team_A, team_B, score_A, score_B) VALUES "
#     for match in matches:
#         values = f"('{match.teamA}', '{match.teamB}', {match.scoreA}, {match.scoreB}), "
#         query += values
#         counter += 1
#     query = query[:-2]
#     # print(query)
#     cursor.execute(query)
#     print(f"{counter} match results have been inserted")
