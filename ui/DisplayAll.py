

class DisplayAll():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def view_all(self):
        while True:
            print("""
            1. View all players
            2. View all teams and their players
            3. View all clubs, their teams and all players in each team

            'q' Logout
            """)
            player_input = input("Enter option: ")
            if player_input == '1':
                self.display_all_players(self.logic_wrapper.get_all_players())
            elif player_input == '2':
                self.display_all_teams(self.logic_wrapper.get_all_teams())
            elif player_input == '3':
                self.display_all_clubs(self.logic_wrapper.get_all_clubs())
            elif player_input == 'q':
                return
    
    def display_player(self, player):
        print(player)
    
    def display_all_players(self, players):
        for player in players:
            print("Name:", player.name + ",", " ID:", player.nid)
            
    
    def display_team(self, team):
        cap = team.captain
        print("\nTeam:", team.name)
        print("""
{}

    {}  {} {}""".format("Team Captain:", (cap.name + ","), "ID: ", cap.nid))
        print("\nMembers:\n")
        for player in team.players:
            print("    {}".format(player.name))
        print("_ "*18)
    
    def display_all_teams(self, teams):
        for team in teams:
            self.display_team(team)
    
    def display_club(self, club):
        print("\nClub:", club.name)
        print("_"*30)
        for team in club.teams:
            self.display_team(team)
    
    def display_all_clubs(self, clubs):
        for club in clubs:
            self.display_club(club)

    
