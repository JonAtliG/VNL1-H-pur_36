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
        2. Choose League    
        'q' to logout
              """)
    
    def __league_options(self):
        print("""
    Please select an option:
        1. Change match
        2. Add teams to League
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
    
    def __display_league_names(self) -> None:
        [print(league.name) for league in self.logic_wrapper.get_all_leagues()]
    
    def input_prompt(self):
        while True:
            self.__options()
            option = input("Select an option: ")
            if option == "q":
                return
            elif option == "1":
                self.__create_league()
            elif option == "2":
                self.__display_league_names()
            else:
                input("Invalid option, click enter to continue.")
    
    def League_input_prompt(self):
        while True:
            self.__options()
            option = input("Select an option: ")
            if option == '1':
                #self.__create_league()
                print("1.") # match_ID 1
                print("2.") #match_ID 2
                match_option = input("Enter number of match to change: ")
                # þarf að breyta því einhvern veginn svo að 
                # númer verði fleiri eftir hversu margar match eru...
                # og þarf með fleiri "if option == 1" setningar...
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
        
