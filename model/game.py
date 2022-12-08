class Game():
    def __init__(self, id = None, home_players = None, away_players = None, home_player_score = None, away_player_score = None, game_type = None, player_count: int = None, played = False) -> None:
        self.id = id
        self.home_players = home_players
        self.away_players = away_players
        self.home_player_score = home_player_score
        self.away_player_score = away_player_score
        self.game_type = game_type
        self.player_count = player_count
        self.played = played
 