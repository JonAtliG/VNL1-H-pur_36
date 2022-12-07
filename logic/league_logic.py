from model.league import League

class League_Logic():
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
    
    def add_leage(self, league: League) -> None:
        self.data_wrapper.add_league(league)
