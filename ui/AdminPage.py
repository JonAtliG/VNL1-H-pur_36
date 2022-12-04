#from MainMenu import MainMenu?
#from DisplayCTP import DisplayCTP
from model.player import Player
from model.club import Club
#from that other thing import another thing
#etc

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
                #host = create_host()

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
                #team_list.append(team)
                #return team

            elif choice == '4':
                pass
                club = Club()
                club.name = input("Enter club name: ")
                #Logic_Wrapper.create_club(club)
                #create_club = create_club()
                #club_list.append(club)
                #return club?? or create_club

            elif choice == '5':
                pass
                #display current tournament information

            elif choice == '6':
                pass
                #view = DisplayCTP("club list", "team list", "player list")

            elif choice == 'q':
                return

            else:
                input("Invalid option, click enter to continue.")
