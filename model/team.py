from model.player import Player

class Team():
    def __init__(self, name: str = None, captain: Player = None, players: list = [], club: str = "No club") -> None:
        '''Constructor for Team class.'''
        self.name = name
        self.captain = captain
        self.players = players
        self.club = club