from model.player import Player

class Player_Data():
    def __init__(self):
        self.file_name = "data/files/players.csv"


    def add_player(self, player):
        with open(self.file_name, "a") as csv:
            csv.write(player.name + ";" + player.nid + ";" + player.mail + ";" + player.birthdate + ";" + player.team + "\n")


    def get_players(self):
        players = []
        with open(self.file_name, "r") as csv:
            for i in csv:
                line = i.strip("\n").split(";")
                players.append(Player(line[0], line[1], line[2], line[3]))
        return players




#class Players():
#    def __init__(self, name, nid, mail, birthdate, team):
#        self.name = name
#        self.nid = nid
#        self.mail = mail
#        self.birthdate = birthdate
#        self.team = team
#
#
#    def add_player(self):
#        with open("files/players.csv", "a") as csv:
#            csv.write(self.name + ";" + self.nid + ";" + self.mail + ";" + self.birthdate + ";" + self.team + "\n")
#
#
#    def get_players():
#        players = []
#        with open("files/players.csv", "r") as csv:
#            for i in csv:
#                line = i.strip("\n").split(";")
#                players.append(line)
#        return players