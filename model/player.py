class Player():
    def __init__(self, name = "No name" , NID = "No ID", mail = "No mail", birthdate = "No birthdate", phone = "No phone", address = "No address", team = "No team"):
        '''Constructor for Player class.'''
        self.name = name
        self.nid = NID
        self.mail = mail
        self.birthdate = birthdate
        self.phone = phone
        self.address = address
        self.team = team
        
    def __str__(self):
        '''Returns the player as a string'''
        return f"Name: {self.name}, NID: {self.nid}, Mail: {self.mail}, Birthdate: {self.birthdate}"
