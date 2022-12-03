class Club():
    def __init__(self, name = None, teams = [], address = None, phone = None) -> None:
        self.name = name
        self.teams = teams
        self.address = address
        self.phone = phone
    
    def __str__(self):
        ret = self.name = "\n"
        ret += "\n".join(self.teams)
        return ret