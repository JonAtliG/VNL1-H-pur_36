class GuestDefault():

    def __str__(self) -> str:
        
        return f"{self.guestpage_output()}{self.input_prompt()}"

    def guestpage_output(self) -> str:
        print("Welcome, Guest")
        print("""Please select one of the options:
        1. View Tournament
        2. Teams and clubs
        3. Players and Team Captains
        
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
        if choice == '1':
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