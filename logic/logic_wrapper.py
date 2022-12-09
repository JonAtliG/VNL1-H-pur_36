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
from logic.input_logic import Input_Validator
class Logic_Wrapper():
    def __init__(self):
        '''Constructor for Logic_Wrapper class.'''
        self.__data_wrapper = Data_Wrapper()
        self.__admin_logic = Admin_Logic(self.__data_wrapper)
        self.__host_logic = Host_logic(self.__data_wrapper)
        self.club_logic = Club_Logic(self.__data_wrapper)
        self.team_logic = Team_Logic(self.__data_wrapper)
        self.player_logic = Player_Logic(self.__data_wrapper)
        self.league_logic = League_Logic(self.__data_wrapper)
        self.match_logic = Match_Logic(self.__data_wrapper)
        self.game_logic = Game_Logic(self.__data_wrapper)
        self.input_validator = Input_Validator()
    
    ### Admin logic
    def verify_admin_id(self, ID):
        '''Returns True if the ID is correct, False otherwise.'''
        return self.__admin_logic.verify_ID(ID)
    
    def verify_admin_password(self, password):
        '''Returns True if the password is correct, False otherwise.'''
        return self.__admin_logic.verify_Password(password)
    
    ### Host logic
    def verify_host_id(self, id: str) -> bool:
        '''Returns True if the ID is correct, False otherwise.'''
        return self.__host_logic.verify_id(id)
    
    def get_host_by_id(self, id: str) -> Host:
        '''Returns the host with the given ID.'''
        return self.__host_logic.get_host_by_id(id)
    
    def get_host_by_league_name(self, name: str) -> Host:
        '''Returns the host with the given league name.'''
        return self.__host_logic.get_host_by_league_name(name)
    
    def add_host(self, host: Host):
        '''Adds the given host to the database.'''
        self.__host_logic.add_host(host)
    
    def update_host(self, host: Host):
        '''Updates the given host in the database.'''
        self.__host_logic.update_host(host)
    
    ### Club Logic
    def __get_club_by_data(self, data: list) -> Club:
        if data[1] == "No teams":
            teams = "No teams"
        else:
            teams = [self.get_team_by_name(name) for name in data[1].split(",")]
        return self.club_logic.make_club_object(data, teams)

    def __get_club_data_by_name(self, name: str) -> list:
        '''Returns the club data with the given name.'''
        return self.club_logic.get_club_data_by_name(name)
    
    def __get_all_club_data(self) -> list:
        '''Returns all club data.'''
        return self.club_logic.get_all_club_data()
    
    def get_club_by_name(self, name: str) -> Club:
        '''Returns the club with the given name.'''
        club_data = self.__get_club_data_by_name(name)
        return self.__get_club_by_data(club_data)
    
    def get_all_clubs(self) -> list:
        '''Returns all clubs.'''
        all_club_data = self.__get_all_club_data()
        return [self.__get_club_by_data(club_data) for club_data in all_club_data]
    
    def add_team_to_club(self, club: Club, team: Team) -> Club:
        '''Adds the given team to the given club.'''
        self.club_logic.add_team_to_club(club, team)
    def add_team_to_club(self, club: Club, team: Team) -> Team:
        return self.club_logic.add_team_to_club(club, team)
    
    def update_club(self, club: Club):
        '''Updates the given club in the database.'''
        self.club_logic.update_club(club)
    
    def add_club(self, club: Club) -> None:
        '''Adds the given club to the database.'''
        self.club_logic.add_club(club)
    
    ### Team Logic
    def __get_team_by_data(self, data: list) -> Team:
        '''Returns team object made from the data'''
        return self.team_logic.make_team_object(data, self.get_player_by_id(data[1]), self.get_players_by_ids(data[2]))
    
    def set_team_club(self, team: Team, club_name: str):
        '''Returns the team with the club set'''
        return self.team_logic.set_club(team, club_name)

    def get_teams_not_in_club(self) -> list:
        '''returns list of teams that are not in a club'''
        team_data = self.team_logic.get_team_data_not_in_club()
        return [self.__get_team_by_data(data) for data in team_data]

    def get_team_by_name(self, name: str) -> Team:
        '''Returns team object of the team with the given name'''
        team_data = self.team_logic.get_team_data_by_name(name)
        return self.__get_team_by_data(team_data)
    
    def get_teams_by_names(self, names: str) -> list:
        '''Returns a list of teams with the given names.'''
        return [self.get_team_by_name(name) for name in names.split(",")]
    
    def get_all_teams(self) -> list:
        '''Returns all teams.'''
        all_team_data = self.team_logic.get_all_team_data()
        return [self.team_logic.make_team_object(team_data, self.get_player_by_id(team_data[1]), self.get_players_by_ids(team_data[2])) for team_data in all_team_data]
    
    def make_team_captain(self, team: Team, player: Player) -> Team:
        '''Makes the given player the captain of the given team.'''
        return self.team_logic.add_player_to_team(team, player)
    
    def add_player_to_team(self, team: Team, player: Player) -> Team:
        '''Adds the given player to the given team.'''
        return self.team_logic.add_player_to_team(team, player)
    
    def update_team(self, team: Team) -> None:
        '''Updates the given team in the database.'''
        self.team_logic.update_team(team)
    
    def add_team(self, team: Team) -> None:
        '''Adds the given team to the database.'''
        self.team_logic.add_team(team)
    
    ### Player Logic
    def is_valid_player_id(self, id: str) -> bool:
        '''Returns True if the ID is valid, False otherwise.'''
        return self.player_logic.is_valid_id(id)
    
    def get_player_by_id(self, id: str) -> Player:
        '''Returns the player with the given ID.'''
        return self.player_logic.get_player_by_id(id)
    
    def get_players_by_ids(self, ids: str) -> list:
        '''Returns a list of players with the given IDs.'''
        return [self.player_logic.get_player_by_id(id) for id in ids.split(",")]
    
    def get_all_players(self) -> list:
        '''Fetches list of all players from player_logic and forwards to ui layer'''
        return self.player_logic.get_all_players()
    
    def update_player(self, player: Player) -> None:
        '''Recieves player from player_logic and forwards to data layer'''
        self.player_logic.update_player(player)
    
    def add_player(self, player: Player) -> None:
        '''Recieves player from player_logic and forwards to data layer'''
        self.player_logic.add_player(player)
    
    ### League Logic
    def __get_league_data_by_name(self, name) -> list:
        '''Returns the league data with the given name.'''
        return self.league_logic.get_league_data_by_name(name)
    
    def __get_all_league_data(self) -> list:
        '''Returns all league data.'''
        return self.league_logic.get_all_league_data()
    
    def __get_league_by_data(self, data) -> League:
        '''Returns a league object with the given data.'''
        if data[1] != "No teams":
            teams = [self.get_team_by_name(team_name) for team_name in data[1].split(",")]
        else:
            teams = data[1]
        if data[2] == "No matches":
            matches = data[2]
        else:
            matches = [self.get_match_by_id(match_id) for match_id in data[2].split(",")]
        return self.league_logic.create_league_object(data, teams, matches)
    
    def __get_all_league_data_by_team_name(self, name: str) -> list:
        '''Returns all league data with the given team name.'''
        return self.league_logic.get_all_league_data_by_team_name(name)
    
    def get_league_by_name(self, name) -> League:
        '''Returns the league with the given name.'''
        return self.__get_league_by_data(self.__get_league_data_by_name(name))
    
    def get_leagues_by_team_name(self, name):
        '''Returns a list of leagues with the given team name.'''
        return [self.__get_league_by_data(league_data) for league_data in self.__get_all_league_data_by_team_name(name)]
    
    def get_all_leagues(self) -> list:
        '''Returns a list of all leagues.'''
        return [self.__get_league_by_data(league_data) for league_data in self.__get_all_league_data()]
        
    def add_league(self, league: League) -> None:
        '''Adds the given league to the database.'''
        self.league_logic.add_leage(league)
    
    def update_league(self, league: League) -> None:
        '''Updates the given league in the database.'''
        self.league_logic.update_league(league)
    
    ### Match Logic
    def __get_match_data_by_id(self, id):
        '''Returns the match data with the given ID.'''
        return self.match_logic.get_match_data_by_id(id)
    
    def give_match_id(self, match: Match) -> Match:
        '''Returns the match with the given ID.'''
        return self.match_logic.give_match_id(match)
    
    def give_match_games(self, match: Match) -> Match:
        '''Returns the match with the given games.'''
        match.games = self.__create_games_for_match()
        return match
    
    def get_match_by_id(self, id):
        '''Returns the match with the given ID.'''
        match_data = self.__get_match_data_by_id(id)
        home_team = self.get_team_by_name(match_data[1])
        away_team = self.get_team_by_name(match_data[2])
        games = [self.get_game_by_id(game_id) for game_id in match_data[3].split(",")]
        return self.match_logic.create_match_object(match_data, home_team, away_team, games)
    
    def add_match(self, match: Match) -> None:
        '''Adds the given match to the database.'''
        self.match_logic.add_match(match)
    
    def update_match(self, match: Match) -> None:
        '''Updates the given match in the database.'''
        self.match_logic.update_match(match)
    
    ### Game Logic
    def __get_game_data_by_id(self, id):
        '''Returns the game data with the given ID.'''
        return self.game_logic.get_game_data_by_id(id)
    
    def __create_games_for_match(self) -> list:
        '''Returns a list of games for the given match.'''
        return self.game_logic.create_games_for_match()
    
    def set_game_score(self, game, home, away):
        '''Sets the score of the given game.'''
        return self.game_logic.set_game_score(game, home, away)
    
    def get_game_by_id(self, id):
        '''Returns the game with the given ID.'''
        game_data = self.__get_game_data_by_id(id)
        if game_data[1] == "No players":
            home_players = game_data[1]
        else:
            home_players = [self.get_player_by_id(player_id) for player_id in game_data[1].split(",")]
        if game_data[2] == "No players":
            away_players = game_data[2]
        else:
            away_players = [self.get_player_by_id(player_id) for player_id in game_data[2].split(",")]
        return self.game_logic.create_game_object(game_data, home_players, away_players)
    
    def add_game(self, game: Game) -> None:
        '''Adds the given game to the database.'''
        self.game_logic.add_game(game)
    
    def update_game(self, game: Game) -> None:
        '''Updates the given game in the database.'''
        self.game_logic.update_game(game)


    # Input validator
    def validate_date(self, date, low = None, high = None) -> bool:
        '''Returns True if the given date is valid, otherwise False.'''
        return self.input_validator.date(date, low, high)

    def validate_name(self, name) -> bool:
        '''Returns True if the given name is valid, otherwise False.'''
        return self.input_validator.name(name)
    
    def validate_id(self, id) -> bool:
        '''Returns True if the given ID is valid, otherwise False.'''
        return self.input_validator.nid(id)

    def validate_number(self, number, high) -> bool:
        '''Returns True if the given number is valid, otherwise False.'''
        return self.input_validator.number(number, high)
    
    def validate_mail(self, mail) -> bool:
        '''Returns True if the given mail is valid, otherwise False.'''
        return self.input_validator.mail(mail)
    
    def validate_phone(self, phone) -> bool:
        '''Returns True if the given phone is valid, otherwise False.'''
        return self.input_validator.phone(phone)
    
    def validate_birthday(self, birthday) -> bool:
        '''Returns True if the given birthday is valid, otherwise False.'''
        return self.input_validator.birthday(birthday)