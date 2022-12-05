#from ui.DisplayAll import DisplayAll
from logic.logic_wrapper import Logic_Wrapper
from model.player import Player
from model.club import Club
from model.team import Team

class AdminPage():
    
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    #def __str__(self) -> str:
    #    
    #    return f"{self.adminpage_output()}{self.input_prompt()}"

    def adminpage_output(self) -> str:
        print("Welcome, Admin")
        print("""Please select one of the options:
        1. Create Host
        2. Create Player
        3. Create Team
        4. Create Club
        5. View Tournament
        6. View all Teams, Clubs and Players
        
        'q' to Logout
        """)

    def input_prompt(self):
        while True:
            self.adminpage_output()
            choice = input("Select an option: ")

            if choice == '1':
                pass
                #host = Host()
                #host.name = input("Host name: ")
                #host.nid = input("Host ID: ")
                #create host --> applies permission to host ID
                #return to AdminPage
                #If host already exists, print("Host already exists!")

            elif choice == '2':
                player = Player()
                player.name = input("Player name: ")
                player.nid = input("Player SSN: ")
                player.mail = input("E-mail: ")
                player.birthdate = input("Birthdate: ")
                player.team = input("Team name: ")
                print(player)
                self.logic_wrapper.create_player(player)

            elif choice == '3':
                pass
                #team = Team()
                #team.name = input("Enter team name: ")
                #team.captain = input("Enter Team Captain ID: ")
                #team.players = input("Add member (by ID): ")
                #team.club = input("Add team Club: ")
                #self.logic_wrapper.create_team(team)

            elif choice == '4':
                pass
                club = Club()
                club.name = input("Enter club name: ")
                Logic_Wrapper.create_club(club)
                return club

            elif choice == '5':
                pass
                #display current tournament information

            elif choice == '6':
                pass
                #print(DisplayAll())

            elif choice == 'q':
                return

            else:
                input("Invalid option, click enter to continue.")
