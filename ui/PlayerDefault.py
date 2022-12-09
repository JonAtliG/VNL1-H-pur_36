from ui.DisplayAll import DisplayAll
from ui.CaptainDefault import CaptainDefault

class PlayerDefault():

    def __init__(self, logic_connection, ID) -> None:
        self.id = ID
        self.__logic_wrapper = logic_connection
        self.__DisplayAll = DisplayAll(logic_connection)
        self.__player = self.__logic_wrapper.get_player_by_id(ID)
        if self.__player.team != "No team":
            self.__team = self.__logic_wrapper.get_team_by_name(self.__player.team)
            self.__team_name = self.__team.name
            if self.__team.captain.nid == self.__player.nid:
                self.__captain = True
            else:
                self.__captain = False
        else:
            self.__team = "No team"
            self.__team_name = "No team"
            self.__captain = False
    
    def options(self):
        print(f"""
        Welcome {self.__player.name}  - Team: {self.__team_name}

        1. View account information
        2. View all clubs, teams and players""", end = "")
        if self.__captain:
            print("""
        3. Captain page""")
        print("""
        'q' Logout""")

    def input_prompt(self):      
            while True:
                self.options()
                option = input("Enter option: ")

                if option == '1':
                    self.information()
                    go_back = input("\nPress enter to go back")
                elif option == '2':
                    self.__DisplayAll.view_all()
                    continue
                elif option == 'q':
                    return
                elif option == "3":
                    if self.__captain:
                        captain_page = CaptainDefault(self.__player, self.__team, self.__logic_wrapper)
                        captain_page.input_prompt()
                    else:
                        input("Invalid option, press enter to continue: ")
                else:
                    input("Invalid option, press enter to continue: ")



    def information(self):
        print("\nPlayer information:\n")
        print("{:<15} {}".format("Team: ", self.__player.team))
        if self.__team != "No team":
            if self.__captain:
                print("{:<15} {}".format("Team role:", "Captain"))
            else:
                print("{:<15} {}".format("Team role:", "Member"))
        print("{:<15} {}".format("Name:", self.__player.name))
        print("{:<15} {}".format("ID:", self.__player.nid))
        print("{:<15} {}".format("Birthdate:", self.__player.birthdate))
        print("{:<15} {}".format("Address:", self.__player.address))
        print("{:<15} {}".format("Phone:", self.__player.phone))
        print("{:<15} {}".format("E-mail:", self.__player.mail))
        input("Click enter to go back.")
