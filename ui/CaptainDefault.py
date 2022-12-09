class CaptainDefault():
    def __init__(self, player, team, logic_connection) -> None:
        self.__logic__wrapper = logic_connection
        self.__player = player
        self.__team = team
        self.__leagues = self.__logic__wrapper.get_leagues_by_team_name(self.__team.name)
        if len(self.__leagues) > 0:
            self.__league = self.__leagues[0]
        else:
            self.__league = "No league"
    
    def __change_selected_league(self):
        if len(self.__leagues) > 0:
            c = 1
            for league in self.__leagues:
                print(f"{c}. {league.name}, Start date: {league.start_date}, End date: {league.end_date}")
                c += 1
                

    def options(self):
        print(f"""Captain options - Team: {self.__team.name}
        Current league selected: {self.__league}
        Please select an option:
        1. Change selected league
        1. Record match scores
        2. View Teams and Players
        3. See upcoming matches
        'q' to logout.""")

    def input_prompt(self):
        self.options()
        choice = input("Select an option: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == 'q':
            return
        else:
            print("Invalid option")
    