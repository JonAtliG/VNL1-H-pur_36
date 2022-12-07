from ui.DisplayAll import DisplayAll

class PlayerDefault():

    def __init__(self, logic_connection, ID) -> None:
        self.id = ID
        self.logic_wrapper = logic_connection
        self.player = self.logic_wrapper.get_player_by_id(ID)
        self.DisplayAll = DisplayAll(logic_connection)

    def __str__(self) -> str:
        pass

    
    def options(self):
        print("""
        1. View account information
        2. View all clubs, teams and players

        'q' Logout
        """)

    def input_prompt(self):      
            while True:
                self.options()
                option = input("Enter option: ")

                if option == '1':
                    self.information()
                    go_back = input("\nPress enter to go back")
                elif option == '2':
                    self.view_all()
                    continue
                elif option == 'q':
                    return
                else:
                    invalid = input("Invalid option, press enter to continue: ")



    def information(self, ID):
        self.logic_wrapper.get_player_by_id(ID)
        print("\nPlayer information:\n")
        print("{:<15} {}".format("Team: ", self.player.team))
        #if captain: print("Team Captain of", self.player.team)
        print("{:<15} {}".format("Name:", self.player.name))
        print("{:<15} {}".format("ID:", self.player.nid))
        print("{:<15} {}".format("Birthdate:", self.player.birthdate))
        print("{:<15} {}".format("Address:", self.player.address))
        print("{:<15} {}".format("Phone:", self.player.phone))
        print("{:<15} {}".format("E-mail:", self.player.mail))
        
