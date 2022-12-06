

class DisplayAll():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
    
    def display_player(self, player):
        print(player)
    
    def display_all_players(self, players):
        for player in players:
            print("Name:", player.name + ",", " ID:", player.nid)
            
    
    def display_team(self, team):
        cap = team.captain
        print("\n")
        print("Team:", team.name)
        print("""
{}

    {}  {} {}""".format("Team Captain:", cap.name, "ID: ", cap.nid))
        print("\nMembers:\n")
        for player in team.players:
            print("    {}".format(player.name))
    
    def display_all_teams(self, teams):
        for team in teams:
            self.display_team(team)
    
    def display_club(self, club):
        print("\nClub:", club.name)
        for team in club.teams:
            self.display_team(team)
    
    def display_all_clubs(self, clubs):
        for club in clubs:
            self.display_club(club)
