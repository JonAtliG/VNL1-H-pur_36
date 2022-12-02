#from MainMenu import MainMenu?
#from that other thing import another thing
#etc

class AdminPage():


    def __str__(self) -> str:
        pass
        #return f"{self.adminpage_output()}{self.input_prompt()}"

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
        choice = input("Select an option: ")
        #if option 1, 2, 3, 4, run programs for 1, 2, 3, 4
        #if option 5, 6, run display for 5, 6
        if choice == '1':
            pass
            #host = create_host()
        elif choice == '2':
            pass
            #player = Player()
            #player.name = input name
            #player.address = input address
            #player.email = etc
            #player.telephone = 
            #player.mobile = 
            #player = create_player()
            #list_of_players.append(player)
            #return player
        if choice == '3':
            pass
            #list_of_teams.append(team)
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
            pass # team, clubs, players
        elif choice == 'q':
            pass #go back to main menu if possible?
        else:
            print("Invalid option")
