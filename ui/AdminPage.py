#from MainMenu import MainMenu?
from CreateTeam import CreateTeam
from CreateClub import CreateClub
#from that other thing import another thing
#etc

class AdminPage():

    def __init__(self) -> None:
        pass #no arguments held eg? User/pass?

    def __str__(self) -> str:
        
        return f"{self.adminpage_output()}{self.input_prompt()}"

    def adminpage_output(self) -> str:
        print("Welcome, Admin")
        print("""Please select one of the options:
        1. Create Host
        2. Create Player
        3. Create Team
        4. Create Club
        5. View Current Tournament
        6. View all Teams, Clubs and Players
        
        'q' to Logout
        """)

    def input_prompt(self):
        choice = input("Select an option: ")
        #if option 1, 2, 3, 4, run programs for 1, 2, 3, 4
        #if option 5, 6, run display for 5, 6
        #if choice == '1':
            #create host
        #elif choice == '2':
            #create player (playerinfo??)
        if choice == '3':
            create_team = CreateTeam()
            print(create_team)
        elif choice == '4':
            create_club = CreateClub()
            print(create_club)
        #elif choice == '5':
            #display current tournament information
        elif choice == 'q':
            pass #go back to main menu if possible?
        else:
            print("Invalid option")
