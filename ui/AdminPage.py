from ui.DisplayAll import DisplayAll
from model.player import Player
from model.club import Club
from model.team import Team

class AdminPage():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        self.display_all = DisplayAll(logic_connection)

    def adminpage_output(self) -> str:
        print("Welcome, Admin")
        print("""Please select one of the options:
        1. Set host privileges
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
                self.set_host_privileges()
            elif choice == '2':
                self.create_player()
            elif choice == '3':
                self.create_team()
            elif choice == '4':
                self.create_club()
            elif choice == '5':
                pass
                #display current tournament information
            elif choice == '6':
                self.DisplayAll.view_all()
            elif choice == 'q':
                return

            else:
                input("Invalid option, click enter to continue.")
    
    def set_host_privileges(self):
        player_id = input("Enter player ID: ")
        player = self.logic_wrapper.get_player_by_id(player_id)
        if player.host:
            print(f"{player.name} currently has host privileges, do you want to remove them?")
            choice = input("y/n: ")
            if choice == "y":
                player.host = False
                self.logic_wrapper.update_player(player)
        else:
            print(f"{player.name} currently does not have host privileges, do you want to give them?")
            choice = input("y/n: ")
            if choice == "y":
                player.host = True
                self.logic_wrapper.update_player(player)
    
    def create_player(self):
        player = Player()
        player.name = input("Player name: ")
        player.nid = input("Player SSN: ")
        player.mail = input("E-mail: ")
        player.birthdate = input("Birthdate: ")
        player.team = input("Team name: ")
        self.logic_wrapper.add_player(player)
    
    def create_team(self):
        team = Team()
        team.name = input("Enter Team Name: ")
        while True:
            add_player = input("Add player? (y/n): ")
            if add_player == 'y':
                player_id = input("Enter player ID: ")
                #self.logic_wrapper.add_player_to_team(_______)
            elif add_player == 'n':
                break
            #team = self.logic_wrapper.add_player_to_team(team, self.logic_wrapper.get_player_by_id(add_player))
            self.displayall.display_team(team)
        team.captain = self.logic_wrapper.get_player_by_id(input("Make Team Captain (ID): "))
        #add captain privileges to ID
        team.club = input("Add team Club: ")
        self.logic_wrapper.add_team(team)
        # Eftir að gera check á hvort captain, players og club eru til
    
    def create_club(self):
        club = Club()
        club.name = input("Enter club name: ")
        club.address = input("Enter address: ")
        club.phone = input("Enter phone number: ")
        self.logic_wrapper.add_club(club)
    
