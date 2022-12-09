files = ["data/files/admin_data.csv", "data/files/club_data.csv", "data/files/game_data.csv", "data/files/host_data.csv", "data/files/league_data.csv", "data/files/match_data.csv", "data/files/player_data.csv", "data/files/team_data.csv"]
backupfiles = ["data/files_backup/admin_data.csv", "data/files_backup/club_data.csv", "data/files_backup/game_data.csv", "data/files_backup/host_data.csv", "data/files_backup/league_data.csv", "data/files_backup/match_data.csv", "data/files_backup/player_data.csv", "data/files_backup/team_data.csv"]

for i, file in enumerate(files):
    file_data = []
    with open(backupfiles[i], "r") as csv:
        for line in csv.readlines():
            file_data.append(line)
    with open(file, "w") as csv:
        for i in file_data:
            csv.write(i)
print("Done")