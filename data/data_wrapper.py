from data.admin_data import Admin_Data
from data.host_data import Host_Data
from data.club_data import Club_Data
from data.team_data import Team_Data
from data.player_data import Player_Data
from data.league_data import League_Data
from data.match_data import Match_Data
from data.game_data import Game_Data
from data.teams_in_tournament import Registered_Teams
from data.scores import Scores

class Data_Wrapper:
    def __init__(self):
        '''Constructor for Data_Wrapper class.'''
        self.admin_data = Admin_Data()
        self.host_data = Host_Data()
        self.club_data = Club_Data()
        self.team_data = Team_Data()
        self.player_data = Player_Data()
        self.teams_in_tournament = Registered_Teams()
        self.scores = Scores()
        self.leage_data = League_Data()
        self.match_data = Match_Data()
        self.game_data = Game_Data()
   
   ### Admin data 
    def get_admin_id(self):
        '''Returns the ID of the admin.'''
        return self.admin_data.get_ID()
    
    def get_admin_password(self):
        '''Returns the password of the admin.'''
        return self.admin_data.get_password()
    
    ### Host data
    def verify_host_id(self, id):
        '''Returns True if the ID is correct, False otherwise.'''
        return self.host_data.verify_id(id)
    
    def get_host_data_by_id(self, id):
        '''Returns the host data of the host with the given ID.'''
        return self.host_data.get_host_data_by_id(id)
    
    def get_host_data_by_league_name(self, name):
        '''Returns the host data of the host with the given league name.'''
        return self.host_data.get_host_data_by_league_name(name)
    
    def add_host(self, host):
        '''Adds a host to the host data.'''
        self.host_data.add_host(host)
    
    def update_host(self, host):
        '''Updates the host data.'''
        self.host_data.update_host(host)
    
    ### Club data
    def get_club_data_by_name(self, name: str) -> list:
        '''Returns the club data of the club with the given name.'''
        return self.club_data.get_club_data_by_name(name)
    
    def get_all_club_data(self) -> list:
        '''Returns all club data.'''
        return self.club_data.get_all_club_data()
    
    def update_club(self, club):
        '''Updates the club data.'''
        self.club_data.update_club(club)
    
    def add_club(self, club):
        '''Adds a club to the club data.'''
        self.club_data.add_club(club)
    
    
    ### Team data
    def get_teams(self):
        '''Returns all teams in the tournament.'''
        return self.teams_in_tournament.get_teams()

    def get_team_data_not_in_club(self) -> list:
        '''Returns team data for teams not in a club'''
        return self.team_data.get_team_data_not_in_club()
    
    def get_team_data_by_name(self, name):
        '''Returns the team data of the team with the given name.'''
        return self.team_data.get_team_data_by_name(name)
    
    def get_all_team_data(self):
        '''Returns all team data.'''
        return self.team_data.get_all_team_data()
    
    def update_team(self, team) -> None:
        '''Updates the team data.'''
        self.team_data.update_team(team)
    
    def add_team(self, team) -> None:
        '''Adds a team to the team data.'''
        self.team_data.add_team(team)
    
    ### Player data
    def is_valid_player_id(self, id):
        '''Returns True if the ID is valid, False otherwise.'''
        return self.player_data.is_valid_id(id)
    
    def get_all_player_data(self):
        '''Returns all player data.'''
        return self.player_data.get_all_player_data()
    
    def get_player_data_by_id(self, id):
        '''Returns the player data of the player with the given ID.'''
        return self.player_data.get_player_data_by_id(id)
    
    def update_player(self, player):
        '''Updates the player data.'''
        self.player_data.update_player(player)
        
    def add_player(self, player):
        '''Adds a player to the player data.'''
        self.player_data.add_player(player)
    
    ### League Data
    def get_league_data_by_name(self, name) -> list:
        '''Returns the league data of the league with the given name.'''
        return self.leage_data.get_league_data_by_name(name)
    
    def get_all_league_data_by_team_name(self, name: str) -> list:
        '''Returns all league data of the team with the given name.'''
        return self.leage_data.get_all_league_data_by_team_name(name)
    
    def get_all_league_data(self) -> list:
        '''Returns all league data.'''
        return self.leage_data.get_all_league_data()
    
    def add_league(self, league) -> None:
        '''Adds a league to the league data.'''
        self.leage_data.add_league(league)
    
    def update_league(self, league) -> None:
        '''Updates the league data.'''
        self.leage_data.update_league(league)
    
    ### Match Data
    def get_match_data_by_id(self, id) -> list:
        '''Returns the match data of the match with the given ID.'''
        return self.match_data.get_match_data_by_id(id)
    
    def get_all_match_data_by_league_name(self, name) -> list:
        '''Returns all match data of the league with the given name.'''
        league_data = self.get_league_data_by_name(name)
        match_data = []
        for match_id in league_data[2].split(","):
            match_data.append(self.get_match_data_by_id(match_id))
        return match_data

    def get_all_match_data(self) -> list:
        '''Returns all match data.'''
        return self.match_data.get_all_match_data()

    def get_all_match_ids(self) -> list:
        '''Returns all match IDs.'''
        return self.match_data.get_all_match_ids()
    
    def add_match(self, match):
        '''Adds a match to the match data.'''
        self.match_data.add_match(match)
    
    def update_match(self, match):
        '''Updates the match data.'''
        self.match_data.update_match(match)
    
    ### Game Data
    def get_all_game_ids(self):
        '''Returns all game IDs.'''
        return self.game_data.get_all_game_ids()
    
    def get_game_data_by_id(self, id):
        '''Returns the game data of the game with the given ID.'''
        return self.game_data.get_game_data_by_id(id)
    
    def get_all_game_data_by_match_id(self, id):
        '''Returns all game data of the match with the given ID.'''
        match_data = self.get_match_data_by_id(id)
        return [self.get_game_data_by_id(id) for id in match_data[3].split(",")]
    
    def get_all_game_data(self):
        '''Returns all game data.'''
        return self.game_data.get_all_game_data()
    
    def add_game(self, game):
        '''Adds a game to the game data.'''
        self.game_data.add_game(game)
    
    def update_game(self, game):
        '''Updates the game data.'''
        self.game_data.update_game(game)
    