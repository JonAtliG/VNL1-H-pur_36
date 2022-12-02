class Club:
    def __init__(self):
        self.file_name = "files/clubs.csv"
    
    def get_all_clubs(self):
        clubs = []
        with open(self.file_name, "r") as txt:
            for i in txt:
                line = i.strip("\n").split(";")
                teams = []
                for j in range(int(line[0])):
                    teams.append(line[j+2])
                clubs.append([line[1], teams])
            return clubs
    
    def get_teams_by_club(self, club_name):
        clubs = self.get_all_clubs()
        for i in clubs:
            if i[0] == club_name:
                return i[1]
        return None
    
    def add_club(self, club_name, teams):
        with open(self.file_name, "a") as csv:
            csv.write(str(len(teams)) + ";" + club_name + ";" + ";".join(teams) + "\n")
    
    def add_teams_to_club(self, club_name, teams):
        clubs = self.get_all_clubs()
        for i in clubs:
            if i[0] == club_name:
                i[1].extend(teams)
                with open(self.file_name, "w") as csv:
                    for j in clubs:
                        csv.write(str(len(j[1])) + ";" + j[0] + ";" + ";".join(j[1]) + "\n")
                return True
        return False