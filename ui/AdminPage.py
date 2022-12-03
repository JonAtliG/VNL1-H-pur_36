#from MainMenu import MainMenu?
#from DisplayCTP import DisplayCTP
from logic.logic_wrapper import Logic_Wrapper
from model.player import Player
from model.club import Club
#from that other thing import another thing
#etc

class AdminPage():


    def __str__(self) -> str:
        
        return f"{self.adminpage_output()}{self.input_prompt()}"

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

            club_list = []
            team_list = []
            player_list = []

            choice = input("Select an option: ")

            if choice == '1':
                pass
                #host = create_host()

            elif choice == '2':
                player = Player()
                player.name = input()
                player.SSN = input()
                player.address = input()
                player.email = input()
                player.telephone = input()
                player.mobile = input()
                Logic_Wrapper.create_player(player)
                #player = create_player()
                #player_list.append(player)
                #return player

            elif choice == '3':
                pass
                #team_list.append(team)
                #return team

            elif choice == '4':
                pass
                club = Club()
                club.name = input("Enter club name: ")
                Logic_Wrapper.create_club(club)
                #create_club = create_club()
                #club_list.append(club)
                #return club?? or create_club

            elif choice == '5':
                pass
                #display current tournament information

            elif choice == '6':
                view = DisplayCTP("club list", "team list", "player list")

            elif choice == 'q':
                pass #go back to main menu if possible?

            else:
                print("Invalid option")
