class Registered_Teams():
    def __init__(self):
        self.file_name = "files/registered_teams.csv"


    def get_teams(self):
        teams = []
        with open(self.file_name, "r") as csv:
            c = 0
            for i in csv:
                if c == 0:
                    league = i.strip("\n")
                elif c % 6 == 2:
                    team = [i.strip("\n")]
                elif c % 6 in [3, 4, 5]:
                    team.append(i.strip("\n").split(";"))
                elif c % 6 == 0:
                    team.append(i.strip("\n").split(";")) 
                    teams.append(team) 
                c += 1
            return teams
    
    def add_team(self, team):
        with open(self.file_name, "a") as csv:
            csv.write("\n" + team[0] + "\n")
            csv.write(";".join(team[1]) + "\n")
            csv.write(";".join(team[2]) + "\n")
            csv.write(";".join(team[3]) + "\n")
            csv.write(";".join(team[4]) + "\n")