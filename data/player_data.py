from model.player import Player

class Player_Data():
    def __init__(self):
        self.file_name = "data/files/players.csv"


    def add_player(self, player):
        with open(self.file_name, "a") as csv:
            csv.write(player.name + ";" + player.nid + ";" + player.mail + ";" + player.birthdate + ";" + player.phone + ";" + player.address + ";" + player.team + "\n")
    
    def get_player_by_id(self, id):
        with open(self.file_name, "r") as csv:
            for i in csv.readlines()[1:]:
                line = i.split(";")
                if line[1] == id:
                    return Player(line[0], line[1], line[2], line[3],line[4],line[5], line[6])

    def get_players(self):
        players = []
        with open(self.file_name, "r") as csv:
            for i in csv.readlines()[1:]:
                line = i.strip("\n").split(";")
                players.append(Player(line[0], line[1], line[2], line[3],line[4],line[5], line[6]))
        return players
