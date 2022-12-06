

class DisplayAll():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
    
    def display_player(self, player):
        print(player)
    
    def display_all_players(self, players):
        for player in players:
            print(player)
    
    def display_team(self, team):
        print(team.name)
        print(f"{team.captain}:Captain")
        for player in team.players:
            print(f"{player}:Member")
    
    def display_all_teams(self, teams):
        for team in teams:
            self.display_team(team)
    
    def display_club(self, club):
        print(club.name)
        for team in club.teams:
            self.display_team(team)
    
    def display_all_clubs(self, clubs):
        for club in clubs:
            self.display_club(club)

    