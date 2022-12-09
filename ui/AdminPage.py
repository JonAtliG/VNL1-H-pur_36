from ui.Display_Information import Display_Information
from model.player import Player
from model.club import Club
from model.team import Team
from model.host import Host

class AdminPage():
    def __init__(self, logic_connection) -> None:
        '''Constructor for AdminPage class.'''
        self.__logic_wrapper = logic_connection
        self.__display_information = Display_Information(logic_connection)

    def adminpage_output(self) -> str:
        '''Prints the admin page menu.'''
        print("_"*30)
        print("Welcome, Admin")
        print("""Please select one of the options:
        1. Create Host
        2. Create Player
        3. Create Team
        4. Create Club
        5. Add team to club
        6. View all Teams, Clubs and Players
        7. View leagues
        
        'q' to Logout
        """)

    def input_prompt(self):
        '''Prompts the user for input and returns the input.'''
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
                self.add_team_to_club()
            elif choice == '6':
                self.__display_information.view_all()
            elif choice == "7":
                self.__display_information.display_leagues()
            elif choice == 'q':
                return

            else:
                input("Invalid option, click enter to continue:")
    
    def create_host(self):
        '''Creates a host object and adds it to the data layer.'''
        host = Host()
        while True:
            host.name = input("Enter Host Name: ")
            if self.__logic_wrapper.validate_name(host.name):
                break
            else:
                input("Invalid name, click enter to continue.")
        while True:
            host.id = input("Enter Host ID: ")
            if self.__logic_wrapper.validate_id(host.id):
                break
            else:
                input("Invalid ID, click enter to continue.")
                
        self.__logic_wrapper.add_host(host)
    
    def create_player(self):
        '''Creates a player object and adds it to the data layer.'''
        player = Player()
        while True:
            player.name = input("Enter Player Name: ")
            if self.__logic_wrapper.validate_name(player.name):
                break
            else:
                input("Invalid name, click enter to continue.")
        while True:
            player.nid = input("Player SSN: ")
            if self.__logic_wrapper.validate_id(player.nid):
                break
            else:
                input("Invalid SSN, click enter to continue.")
        while True:
            player.mail = input("E-mail: ")
            if self.__logic_wrapper.validate_mail(player.mail):
                break
            else:
                input("Invalid e-mail, click enter to continue.")
        while True:
            player.phone = input("Phone number: ")
            if self.__logic_wrapper.validate_phone(player.phone):
                break
            else:
                input("Invalid phone number, click enter to continue.")
        
        while True:
            player.birthdate = input("Birthdate (dd.mm.yyyy): ")
            if self.__logic_wrapper.validate_birthday(player.birthdate):
                break
            else:
                input("Invalid birthdate, click enter to continue.")
        
        while True:
            player.address = input("Address: ")
            if self.__logic_wrapper.validate_name(player.address):
                break
            else:
                input("Invalid address, click enter to continue.")

        player.team = "No team"
        input("Player created, click enter to continue.")
        self.__logic_wrapper.add_player(player)
    
    def create_team(self):
        '''Creates a team object and adds it to the data layer.'''
        team = Team()
        while True:
            team.name = input("Enter Team Name: ")
            if self.__logic_wrapper.validate_name(team.name):
                break
            else:
                input("Invalid name, click enter to continue.")
        c = 0
        while c < 4:
            
            if c== 0:
                inp = input("Enter Captain ID or cancel (c): ")
            else:
                inp = input("Enter player ID or cancel (c): ")
            if inp == "c":
                return
            try:
                player = self.__logic_wrapper.get_player_by_id(inp)
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
        self.__logic_wrapper.update_player(team.captain)
        [self.__logic_wrapper.update_player(player) for player in team.players]
        self.__logic_wrapper.add_team(team)
    
    def create_club(self):
        '''Creates a club object and adds it to the data layer.'''
        club = Club()
        while True:
            club.name = input("Enter club name: ")
            if self.__logic_wrapper.validate_name(club.name):
                break
            else:
                input("Invalid name, click enter to continue.")
        while True:
            club.address = input("Enter address: ")
            if self.__logic_wrapper.validate_name(club.address):
                break
            else:
                input("Invalid address, click enter to continue.")
        while True:
            club.phone = input("Enter phone number: ")
            if self.__logic_wrapper.validate_phone(club.phone):
                break
            else:
                input("Invalid phone number, click enter to continue.")
        self.__logic_wrapper.add_club(club)

    def add_team_to_club(self):
        clubs =  self.__logic_wrapper.get_all_clubs()
        c = 1
        for club in clubs:
            print(f"{c}. {club.name}")
            c += 1
        while True:
            choice = input("Choose a club to add a team to, or quit(q): ")
            if self.__logic_wrapper.validate_number(choice, c):
                club = clubs[int(choice) - 1]
                #try:
                teams = self.__logic_wrapper.get_teams_not_in_club()
                #except:
                #    input("There are no teams that are not in a club, click enter to go back")
                #    return
                c = 1
                for team in teams:
                    print(f"{c}. {team.name}")
                    c += 1
                while True:
                    choice = input("Choose a team too add or quit (q): ")
                    if choice == "q":
                        return
                    elif self.__logic_wrapper.validate_number(choice, c):
                        team = teams[int(choice) - 1]
                        team = self.__logic_wrapper.set_team_club(team, club.name)
                        club = self.__logic_wrapper.add_team_to_club(club, team)
                        self.__logic_wrapper.update_club(club)
                        self.__logic_wrapper.update_team(team)
                        input("Team has been added to the club, click enter to continue.")
                        return
            elif choice == "q":
                return
            else:
                print("Invalid input.")
