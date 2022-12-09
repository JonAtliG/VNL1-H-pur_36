class Host():
    def __init__(self, id = None, name: str = "No name", league_names: list = "No leagues") -> None:
        '''Constructor for Host class.'''
        self.id = id
        self.name = name
        self.league_names = league_names