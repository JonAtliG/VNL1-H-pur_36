from ui.DisplayAll import DisplayAll

class HostDefault():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        self.display_information = DisplayAll(logic_connection)

    def options(self):
        print("""
    Please select an option:
        1. Create tournament
        2. Change match
        3. View matches played
        4. View teams and players
        'q' to logout.""")
        print("_"*25)

    def input_prompt(self):
        self.options()
        option = input("Select an option: ")

        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            league = self.logic_wrapper.get_all_leagues()[0]
            self.display_information.display_league_matches(league)
        elif option == '4':
            pass
        elif option == 'q':
            return
        else:
            print("Invalid option")

    def __str__(self) -> str:
        pass
