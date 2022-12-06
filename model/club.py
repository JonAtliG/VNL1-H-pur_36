class Club():
    def __init__(self, name = "No name", teams = "No teams", address = "No address", phone = "No phone") -> None:
        self.name = name
        self.teams = teams
        self.address = address
        self.phone = phone
    
    def __str__(self):
        ret = self.name = "\n"
        ret += "\n".join(self.teams)
        return ret