from model.team import Team
from model.player import Player

class Team_Logic():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
    
    def make_team_object(self, data, captain: Player , players: list):
        team = Team()
        team.name = data[0]
        team.captain = captain
        team.players = players
        team.club = data[3]
        return team
    
    def get_all_team_data(self):
        return self.data_wrapper.get_all_team_data()
    
    def get_team_data_by_name(self, name):
        return self.data_wrapper.get_team_data_by_name(name)
    
    def set_club(self, team: Team, club_name: str) -> Team:
        team.club = club_name
        return team
    
    def make_team_captain(self, team: Team, player: Player) -> Team:
        players = []
        for member in team.players:
            if member == player:
                team.captain = player
            else:
                players.append(member)
        return team
    
    def get_team_data_not_in_club(self) -> list:
        '''Returns list of team data of teams not in a club'''
        return self.data_wrapper.get_team_data_not_in_club()
    
    def add_player_to_team(self, team: Team, player: Player) -> Team:
        if player.team == "No team":
            if team.players == "No players":
                team.players = [player]
            else:
                team.players.append(player)
            player.team = team.name
        return team, player
    
    def update_team(self,team):
        self.data_wrapper.update_team(team)
    
    def add_team(self, team):
        '''Takes in team object and forwards to data layer'''
        self.data_wrapper.add_team(team)