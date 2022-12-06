from ui.DisplayAll import DisplayAll

class PlayerDefault():

    def __init__(self, logic_connection, ID) -> None:
        self.id = ID
        self.logic_wrapper = logic_connection
        self.player = self.logic_wrapper.get_player_by_id(ID)
        self.DisplayAll = DisplayAll(logic_connection)

    def __str__(self) -> str:
        
        return self.options()

    def options(self):
        print("Welcome\n")
        print("""
        1. View player information
        2. View player matches
        3. View all teams, clubs, players
        'q' to quit""")

    def input_prompt(self, ID):
        self.id = ID
        while True:
            option = input("Enter option: ")

            if option == '1':
                self.information(ID)
                continue
            elif option == '2':
                pass
            elif option == '3':
                print("""
                1. View only Players
                2. View Teams and Players
                3. View Clubs, Teams, Players

                'q' to go back
                """)
                player_input = input("Enter option: ")
                if input == '1':
                    self.display_all.display_all_players(self.logic_wrapper.get_all_players())
                elif input == '2':
                    self.display_all.display_all_teams(self.logic_wrapper.get_all_teams())
                elif input == '3':
                    self.display_all.display_all_clubs(self.logic_wrapper.get_all_clubs())
                continue
            elif option == 'q':
                return
            else:
                invalid = input("Invalid option, press enter to continue: ")


    def information(self, ID):
        self.logic_wrapper.get_player_by_id(ID)
        print("\nPlayer information:\n")
        print("{:>10} {}".format("Team: ", self.player.team))
        print("{:<15} {}".format("Name:", self.player.name))
        print("{:<15} {}".format("ID:", self.player.nid))
        print("{:<15} {}".format("Birthdate:", self.player.birthdate))
        print("{:<15} {}".format("Address:", self.player.address))
        print("{:<15} {}".format("Phone:", self.player.phone))
        print("{:<15} {}".format("E-mail:", self.player.mail))
        
