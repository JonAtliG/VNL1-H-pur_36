class Player():
    def __init__(self, name = None , NID = None, mail = None, birthdate = None, team = None):
        self.name = name
        self.nid = NID
        self.mail = mail
        self.birthdate = birthdate
        self.team = team

    def __str__(self):
        return f"Name: {self.name}, NID: {self.nid}, Mail: {self.mail}, Birthdate: {self.birthdate}"
    
    
    #def makeHost(self):
    #    self.host = True