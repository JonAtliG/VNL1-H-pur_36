from ui.DisplayAll import DisplayAll
from model.player import Player
from model.club import Club
from model.team import Team
from model.host import Host

class AdminPage():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        self.display_all = DisplayAll(logic_connection)

    def adminpage_output(self) -> str:
        print("Welcome, Admin")
        print("""Please select one of the options:
        1. Create Host
        2. Create Player
        3. Create Team
        4. Create Club
        5. View all Teams, Clubs and Players
        
        'q' to Logout
        """)

    def input_prompt(self):
        while True:
            self.adminpage_output()
            choice = input("Select an option: ")
            if choice == '1':
                self.create_host()
                #self.set_host_privileges()
                # enter host ID
                # add host privileges á bara þetta ID
                # svo þegar maður log in by id, með Host ID, þá runnar HostDefault
                pass
            elif choice == '2':
                self.create_player()
            elif choice == '3':
                self.create_team()
            elif choice == '4':
                self.create_club()
            elif choice == '5':
                self.display_all.view_all()                
            elif choice == 'q':
                return

            else:
                input("Invalid option, click enter to continue:")
    
    def create_host(self):
        host = Host()
        host.name = input("Enter Host Name: ")
        host.id = input("Enter Host ID: ")
        self.logic_wrapper.add_host(host)
    
    def create_player(self):
        player = Player()
        player.name = input("Player name: ")
        player.nid = input("Player SSN: ")
        player.mail = input("E-mail: ")
        player.birthdate = input("Birthdate: ")
        player.phone = input("Phone number: ")
        player.address = input("Address: ")
        player.team = "No team"
        self.logic_wrapper.add_player(player)
    
    def create_team(self):
        team = Team()
        team.name = input("Enter Team Name: ")
        
        c = 0
        while c < 4:
            
            if c== 0:
                inp = input("Enter Captain ID: ")
            else:
                inp = input("Enter player ID: ")
            print("Enter 'q' to quit")
            if inp == "q":
                break
            try:
                player = self.logic_wrapper.get_player_by_id(inp)
                if player.team != "No team":
                    print("Person is already in a team")
                    c -= 1
                else:
                    player.team = team.name
                if c == 0:
                    team.captain = player
                else:
                    team.players.append(player)
            except:
                print("Player not found")
                c -= 1
            c += 1
        self.logic_wrapper.update_player(team.captain)
        [self.logic_wrapper.update_player(player) for player in team.players]
        self.logic_wrapper.add_team(team)
    
    def create_club(self):
        club = Club()
        club.name = input("Enter club name: ")
        club.address = input("Enter address: ")
        club.phone = input("Enter phone number: ")
        club.teams = []
        while True:
            add_team = input("Add team? (y/n)")
            if add_team == 'y':
                while True:
                    try:
                        counter = int(input("How many teams do you want to add? (1-5): "))
                        if 1 <= counter <= 5:
                            break
                    except:
                        print("Invalid input")
                
                c = 0
                while c < counter:
                    team_name = input("Enter Team Name: ")
                    print("Enter 'q' to quit")
                    if team_name == "q":
                        break
                    try:
                        team = self.logic_wrapper.get_team_by_name(team_name)
                        if team.club != "No club":
                            print("Team is already in a club")
                            c -= 1
                        else:
                            team.club = club.name
                            self.logic_wrapper.update_team(team)
                            club.teams.append(team)
                    except:
                        print("Team not found")
                        c -= 1
                    c += 1
            
            elif add_team == 'n':
                break

            try:
                if team_name == "q":
                    break
            except:
                pass
        self.logic_wrapper.add_club(club)