from data.data_wrapper import Data_Wrapper
from model.host import Host
from model.club import Club
from model.team import Team
from model.player import Player
from model.league import League
from model.match import Match
from model.game import Game
from logic.admin_logic import Admin_Logic
from logic.host_logic import Host_logic
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
        self.host_logic = Host_logic(self.data_wrapper)
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
    
    ### Host logic
    def verify_host_id(self, id: str) -> bool:
        return self.host_logic.verify_id(id)
    
    def get_host_by_id(self, id: str) -> Host:
        return self.host_logic.get_host_by_id(id)
    
    def get_host_by_league_name(self, name: str) -> Host:
        return self.host_logic.get_host_by_league_name(name)
    
    def add_host(self, host: Host):
        self.host_logic.add_host(host)
    
    def update_host(self, host: Host):
        self.host_logic.update_host(host)
    
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
    
    def add_team_to_club(self, club: Club, team: Team) -> Team:
        self.club_logic.add_team_to_club(club, team)
    
    def update_club(self, club: Club):
        self.club_logic.update_club(club)
    
    def add_club(self, club: Club) -> None:
        self.club_logic.add_club(club)
    
    ### Team Logic
    def get_team_by_name(self, name: str) -> Team:
        team_data = self.team_logic.get_team_data_by_name(name)
        return self.team_logic.make_team_object(team_data, self.get_player_by_id(team_data[1]), self.get_players_by_ids(team_data[2]))
    
    def get_teams_by_names(self, names: str) -> list:
        return [self.get_team_by_name(name) for name in names.split(",")]
    
    def get_all_teams(self) -> list:
        all_team_data = self.team_logic.get_all_team_data()
        return [self.team_logic.make_team_object(team_data, self.get_player_by_id(team_data[1]), self.get_players_by_ids(team_data[2])) for team_data in all_team_data]
    
    def make_team_captain(self, team: Team, player: Player) -> Team:
        return self.team_logic.add_player_to_team(team, player)
    
    def add_player_to_team(self, team: Team, player: Player) -> Team:
        return self.team_logic.add_player_to_team(team, player)
    
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
        self.player_logic.update_player(player)
    
    def add_player(self, player: Player) -> None:
        '''Recieves player from player_logic and forwards to data layer'''
        self.player_logic.add_player(player)
    
    ### League Logic
    def __get_league_data_by_name(self, name) -> list:
        return self.league_logic.get_league_data_by_name(name)
    
    def __get_all_league_data(self) -> list:
        return self.league_logic.get_all_league_data()
    
    def __get_league_by_data(self, data) -> League:
        if data[1] != "No teams":
            teams = [self.get_team_by_name(team_name) for team_name in data[1].split(",")]
        else:
            teams = data[1]
        if data[2] == "No matches":
            matches = data[2]
        else:
            matches = [self.get_match_by_id(match_id) for match_id in data[2].split(",")]
        return self.league_logic.create_league_object(data, teams, matches)
    
    def get_league_by_name(self, name) -> League:
        return self.__get_league_by_data(self.__get_league_data_by_name(name))
    
    def get_all_leagues(self) -> list:
        return [self.__get_league_by_data(league_data) for league_data in self.__get_all_league_data()]
        
    def add_league(self, league: League) -> None:
        self.league_logic.add_leage(league)
    
    def update_league(self, league: League) -> None:
        self.league_logic.update_league(league)
    
    ### Match Logic
    def __get_match_data_by_id(self, id):
        return self.match_logic.get_match_data_by_id(id)
    
    def get_match_by_id(self, id):
        match_data = self.__get_match_data_by_id(id)
        home_team = self.get_team_by_name(match_data[1])
        away_team = self.get_team_by_name(match_data[2])
        games = [self.get_game_by_id(game_id) for game_id in match_data[3].split(",")]
        return self.match_logic.create_match_object(match_data, home_team, away_team, games)
    
    def add_match(self, match: Match) -> None:
        self.match_logic.add_match(match)
    
    def update_match(self, match: Match) -> None:
        self.match_logic.update_match(match)
    
    ### Game Logic
    def __get_game_data_by_id(self, id):
        return self.game_logic.get_game_data_by_id(id)
    
    def get_game_by_id(self, id):
        game_data = self.__get_game_data_by_id(id)
        home_players = [self.get_player_by_id(player_id) for player_id in game_data[1].split(",")]
        away_players = [self.get_player_by_id(player_id) for player_id in game_data[2].split(",")]
        return self.game_logic.create_game_object(game_data, home_players, away_players)
    
    def add_game(self, game: Game) -> None:
        self.game_logic.add_game(game)
    
    def update_game(self, game: Game) -> None:
        self.game_logic.update_game(game)
