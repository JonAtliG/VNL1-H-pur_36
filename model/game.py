class Game():
    def __init__(self, ID = None, home_player = None, away_player = None, home_player_score = None, away_player_score = None, game_type = None, played = False) -> None:
        self.ID = ID
        self.home_player = home_player
        self.away_player = away_player
        self.home_player_score = home_player_score
        self.away_player_score = away_player_score
        self.game_type = game_type
        self.played = played
 