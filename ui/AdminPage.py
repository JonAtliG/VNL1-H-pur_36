#from MainMenu import MainMenu?
from DisplayCTP import DisplayCTP
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
                pass
                #player = Player()
                #player.name =
                #player.address = 
                #player.email = 
                #player.telephone = 
                #player.mobile = 
                #player = create_player()
                #player_list.append(player)
                #return player

            elif choice == '3':
                pass
                #team_list.append(team)
                #return team

            elif choice == '4':
                pass
                #club = Club()
                #club_name = input("Enter club name: ")
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
