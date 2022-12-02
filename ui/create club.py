class Createclub():


    def getname(self):
        clubname= input("Club name: ")
        return clubname

    def getaddress(self):
        clubaddress= input("Club address: ")
        return clubaddress
    
    def getphonenumber(self):
        phonenumber= input("Club phonenumber: ")
        return phonenumber

    def addteam(self, list, name):
        self.list = list
        self.name = name
        list = []
        list.append(name)
        return list



    