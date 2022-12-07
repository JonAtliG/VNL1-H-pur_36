from ui.DisplayAll import DisplayAll
from model.league import League

class HostDefault():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        self.display_information = DisplayAll(logic_connection)

    def __options(self):
        print("""
    Please select an option:
        1. Create League
        2. Change match
        3. View matches played
        4. View teams and players
        'q' to logout.""")
        print("_"*25)
    
    def __create_league(self):
        league = League()
        league.name = input("Enter a name for the league: ")
        league.start_date = input("Enter start date for the league (dd:mm:yy): ")
        league.end_date = input("Enter end date for the league (dd:mm:yy): ")
        self.logic_wrapper.add_league(league)
        

    def input_prompt(self):
        while True:
            self.__options()
            option = input("Select an option: ")
            if option == '1':
                self.__create_league()
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
                input("Invalid option, click enter to continue")
        