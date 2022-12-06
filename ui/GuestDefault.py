from ui.DisplayAll import DisplayAll  

class GuestDefault:

    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        self.display_all = DisplayAll(logic_connection)


    def __str__(self) -> str:
        return self.options(), self.input_prompt()

    def options(self):
        print("""
        Select an option:
            1. View Tournament
            2. View Matches
            3. View Clubs, Teams and Players
            'q' to go back to Main Menu""")

    def input_prompt(self):
        while True:
            self.options()
            option = input("Select an option: ")
            if option == "q":
                return
            elif option == "1":
                view_tournament_page = ViewTournament(self.logic_wrapper)
            elif option == "2":
                view_matches_page = ViewMatches(self.logic_wrapper)
            elif option == "3":
                self.display_all.display_all_clubs(self.logic_wrapper.get_all_clubs())
            else:
                input("Invalid option, click enter to continue.")
