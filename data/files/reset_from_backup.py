files = ["admin_data.csv", "club_data.csv", "game_data.csv", "host_data.csv", "league_data.csv", "match_data.csv", "player_data.csv", "team_data.csv"]
backupfiles = ["files_backup/admin_data.csv", "files_backup/club_data.csv", "files_backup/game_data.csv", "files_backup/host_data.csv", "files_backup/league_data.csv", "files_backup/match_data.csv", "files_backup/player_data.csv", "files_backup/team_data.csv"]

for i, file in enumerate(files):
    file_data = []
    with open(backupfiles[i], "r") as csv:
        for line in csv.readlines():
            file_data.append(line)
    with open(file, "w") as csv:
        for i in file_data:
            csv.write(i)
print("Done")