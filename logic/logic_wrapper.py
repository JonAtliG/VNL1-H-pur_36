from data.data_wrapper import Data_Wrapper
from model.club import Club
from model.team import Team
from model.player import Player
from logic.admin_logic import Admin_Logic
from logic.club_logic import Club_Logic
from logic.team_logic import Team_Logic
from logic.player_logic import Player_Logic
from logic.league_logic import League_Logic
from logic.match_logic import Match_Logic
from logic.game_logic import Game_Logic


class Logic_Wrapper():
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.admin_logic = Admin_Logic(self.data_wrapper)
        self.club_logic = Club_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.player_logic = Player_Logic(self.data_wrapper)
        self.league_logic = League_Logic(self.data_wrapper)
        self.match_logic = Match_Logic(self.data_wrapper)
        self.game_logic = Game_Logic(self.data_wrapper)
    
    ### Admin logic
    def verify_admin_id(self, ID):
        return self.admin_logic.verify_ID(ID)
    
    def verify_admin_password(self, password):
        return self.admin_logic.verify_Password(password)
    
    ### Club Logic
    def __get_club_data_by_name(self, name: str) -> list:
        return self.club_logic.get_club_data_by_name(name)
    
    def __get_all_club_data(self) -> list:
        return self.club_logic.get_all_club_data()
    
    def get_club_by_name(self, name: str) -> Club:
        club_data = self.__get_club_data_by_name(name)
        return self.club_logic.make_club_object(club_data, self.get_teams_by_names(club_data[1]))
    
    def get_all_clubs(self) -> list:
        all_club_data = self.__get_all_club_data()
        return [self.club_logic.make_club_object(club_data, self.get_teams_by_names(club_data[1])) for club_data in all_club_data]
    
    def update_club(self, club: Club):
        self.data_wrapper.update_club(club)
    
    def add_club(self, club: Club) -> None:
        self.data_wrapper.add_club(club)
    
    ### Team Logic
    def get_team_by_name(self, name: str) -> Team:
        team_data = self.team_logic.get_team_data_by_name(name)
        return self.team_logic.make_team_object(team_data, self.get_player_by_id(team_data[1]), self.get_players_by_ids(team_data[2]))
    
    def get_teams_by_names(self, names: str) -> list:
        return [self.get_team_by_name(name) for name in names.split(",")]
    
    def get_all_teams(self) -> list:
        all_team_data = self.team_logic.get_all_team_data()
        return [self.team_logic.make_team_object(team_data, self.get_player_by_id(team_data[1]), self.get_players_by_ids(team_data[2])) for team_data in all_team_data]
    
    def update_team(self, team: Team) -> None:
        self.team_logic.update_team(team)
    
    def add_team(self, team: Team) -> None:
        self.team_logic.add_team(team)
    
    ### Player Logic
    def get_player_by_id(self, id: str) -> Player:
        return self.player_logic.get_player_by_id(id)
    
    def get_players_by_ids(self, ids: str) -> list:
        return [self.player_logic.get_player_by_id(id) for id in ids.split(",")]
    
    def get_all_players(self) -> list:
        '''Fetches list of all players from player_logic and forwards to ui layer'''
        return self.player_logic.get_all_players()
    
    def update_player(self, player: Player) -> None:
        self.data_wrapper.update_player(player)
    
    def add_player(self, player: Player) -> None:
        '''Recieves player from player_logic and forwards to data layer'''
        self.player_logic.add_player(player)

