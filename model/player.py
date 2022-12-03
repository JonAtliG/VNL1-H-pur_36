class Player():
    def __init__(self, name = None , SSN = None, address = None ,mobile = None, telephone = None, email = None):
        self.name = name
        self.SSN =  SSN
        self.address = address
        self.mobile = mobile
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, NID: {self.SSN}, Address: {self.address}, Phone: {self.Phone}"

    def getName(self):
        return self.name
    
    def getNID(self):
        return self.NID
    
    def getAddress(self):
        return self.address
    
    #def makeHost(self):
    #    self.host = True