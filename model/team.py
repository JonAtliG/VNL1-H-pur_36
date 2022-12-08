from model.player import Player

class Team():
    def __init__(self, name: str = None, captain: Player = None, players: list = [], club: str = "No club") -> None:
        self.name = name
        self.captain = captain
        self.players = players
        self.club = club