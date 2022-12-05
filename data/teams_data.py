class Team_Data():
    def __init__(self) -> None:
        self.file_name = "data/files/teams.csv"
    
    def add_team(self, team):
        pass
    
    def get_teams_data(self):
        teams_data = []
        with open(self.file_name, "r") as csv:
            for i in csv.readlines()[1:]:
                teams_data.append(i.split(";"))
                
    def get_team_data_by_name(self, name):
        with open(self.file_name, "r") as csv:
            for i in csv.readlines()[1:]:
                line = i.split(";")
                if line[0] == name:
                    return line
        return False