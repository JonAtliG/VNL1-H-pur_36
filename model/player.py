class Player():
    def __init__(self, name = None , NID = None, address = None ,Phone = None):
        self.name = name
        self.NID =  NID
        self.address = address
        self.Phone = Phone
        self.host = False

    def __str__(self):
        return f"Name: {self.name}, NID: {self.NID}, Address: {self.address}, Phone: {self.Phone}"

    def getName(self):
        return self.name
    
    def getNID(self):
        return self.NID
    
    def getAddress(self):
        return self.address
    
    #def makeHost(self):
    #    self.host = True