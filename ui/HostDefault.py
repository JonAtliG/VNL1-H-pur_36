from ui.DisplayAll import DisplayAll
from model.league import League

class HostDefault():
    def __init__(self, hostid, logic_connection) -> None:
        self.__logic_wrapper = logic_connection
        self.display_information = DisplayAll(logic_connection)
        self.host = self.__logic_wrapper.get_host_by_id(hostid)
    
    def __options(self):
        print("""
    Please select an option:
        1. Create League
        2. Choose League    
        'q' to logout.
              """)
    
    def __create_league(self):
        league = League()
        leagues = self.__logic_wrapper.get_all_leagues()
        
        while True: 
            name = input("Enter a name for the league: ")
            if name not in [league.name for league in leagues]:
                break
            else:
                input("League name already exists, click enter to continue.")
        league.name = name
        league.start_date = input("Enter start date for the league (dd:mm:yy): ")
        league.end_date = input("Enter end date for the league (dd:mm:yy): ")
        league.matchcount = input("Enter number of matches for the league: ")
        league.phone_number = input("Enter phone number for the league: ")
        self.__logic_wrapper.add_league(league)
    
    def __display_league_names(self) -> None:
        if self.host.league_names == "No leagues":
            input("You have no leagues, click enter to continue.")
            return
        print([name for name in self.host.league_names])
        leagues = [self.__logic_wrapper.get_league_by_name(name) for name in self.host.league_names]
        c = 1
        for league in leagues:
            print(f"{c}. {league.name}")
            c += 1
        print(f'"q". Go back')
        league_choice = input("Select a league: ")
        if league_choice == "q":
            return
        elif league_choice.isdigit():
            if 1 <= int(league_choice) < c:
                league = leagues[int(league_choice) - 1]
                print(f"League: {league.name}")
                print("1. Plan upcoming matches")
                print("2. Change time of an upcoming match")
                print("3. Change score of a finished match")
                print("4. Add teams to league")
                print('"q". Go back')
                choice = input("Select an option: ")
                if choice == "1":
                    pass
                elif choice == "2":
                    pass
                elif choice == "3":
                    pass
                elif choice == "4":
                    pass
                elif choice == "q":
                    return
                else:
                    input("Invalid option, click enter to continue.")
        else:
            input("Invalid option, click enter to continue.")
    
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
