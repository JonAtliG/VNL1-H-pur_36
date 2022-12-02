from MainMenu import MainMenu

class CreateTeam():


    def __str__(self) -> str:
        pass # Geta séð Player samkvæmt kennitölu (ID) sem sett er inn)
    #Returnaði listinn úr add_player setur upp

    def get_name(self, name, ):
        name = input("Enter team name: ")
        return name


    def add_player(self, list, ID):
        self.list = list
        self.id = ID
        list = []
        list.append(ID)

        return list
