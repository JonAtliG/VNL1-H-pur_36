class Club():
    def __init__(self, name = "No name", teams = "No teams", address = "No address", phone = "No phone") -> None:
        '''Constructor for Club class.'''
        self.name = name
        self.teams = teams
        self.address = address
        self.phone = phone
    
    def __str__(self):
        '''Returns the club as a string'''
        ret = self.name = "\n"
        ret += "\n".join(self.teams)
        return ret