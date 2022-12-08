from ui.DisplayAll import DisplayAll
from model.league import League
from model.match import Match

class HostDefault():
    def __init__(self, hostid, logic_connection) -> None:
        self.__logic_wrapper = logic_connection
        self.display_information = DisplayAll(logic_connection)
        self.host = self.__logic_wrapper.get_host_by_id(hostid)
    
    def input_prompt(self):
        while True:
                self.__options()
                option = input("Select an option: ")
                if option == "q":
                    return
                elif option == "1":
                    self.__create_league()
                elif option == "2":
                    self.__league_options()
                else:
                    input("Invalid option, click enter to continue.")

    
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
        self.host.league_names.append(league.name)
        self.__logic_wrapper.add_league(league)
        self.__logic_wrapper.update_host(self.host)
    
    def __league_options(self) -> None:
        while True:
            if self.host.league_names == "No leagues":
                input("You have no leagues, click enter to continue.")
                return
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
                    print("1. Plan an upcoming match")
                    print("2. Change time of an upcoming match")
                    print("3. Change score of a finished match")
                    print("4. Add teams to league")
                    print('"q". Go back')
                    choice = input("Select an option: ")
                    if choice == "1":
                        league = self.__create_match(league)
                    elif choice == "2":
                        self.__change_time_of_upcoming_match(league)
                    elif choice == "3":
                        pass
                    elif choice == "4":
                        league = self.__choose_team_to_add(league)
                    elif choice == "q":
                        return
                    else:
                        input("Invalid option, click enter to continue.")
            else:
                input("Invalid option, click enter to continue.")
    
    def __create_match(self, league: League) -> League:
        c = 1
        if league.teams == "No teams" or len(league.teams) < 2:
            input("There are not enough teams in the league to plan a match, click enter to continue.")
            return league
        else:
            match = Match()
            match = self.__logic_wrapper.give_match_id(match)
            for team in league.teams:
                print(f"{c}. {team.name}")
                c += 1
            while True:
                choice = input("Choose a home team for the match or quit (q): ")
                if choice.isdigit():
                    if 0 < int(choice) < c:
                        match.home_team = league.teams[int(choice)-1]
                        c = 1
                        for team in league.teams:
                            if team.name == match.home_team.name:
                                pass
                            else:
                                print(f"{c}. {team.name}")
                                c += 1
                        while True:
                            choice = input("Choose an away team for the match or quit (q): ")
                            if choice.isdigit():
                                if 0 < int(choice) < c:
                                    match.away_team = league.teams[int(choice)-1]
                                    match.date = input("Enter a date for the match (dd.mm.yy): ")
                                    match = self.__logic_wrapper.give_match_games(match)
                                    if league.matches == "No matches":
                                        league.matches = [match]
                                    else:
                                        league.matches.append(match)
                                    print(league.matches)
                                    self.__logic_wrapper.update_league(league)
                                    self.__logic_wrapper.add_match(match)
                                    [self.__logic_wrapper.add_game(game) for game in match.games]
                                    input(f"Match: {match.home_team.name} vs {match.away_team.name}\n Has been added, click enter to continue")
                                    return league
                            elif choice == "q":
                                return league
                            else:
                                print("Invalid choice.")
                elif choice == "q":
                    return league
                print("Invalid choice.")
    
    def __change_time_of_upcoming_match(self, league):
        if league.matches == "No matches":
            input("League has no matches, click enter to continue.")
        else:
            upcoming_matches = []
            for match in league.matches:
                if match.games[0].played:
                    upcoming_matches.append(match)
            if len(upcoming_matches) > 0:
                for i, match in enumerate(upcoming_matches):
                    print(f"{i+1}. {match.home_team.name} vs {match.away_team.name} - Date: {match.date}")
                choice = input("Choose a match to change its date or quit (q): ")
                if choice: # input validator
                    match_to_change = upcoming_matches[int(choice)-1]
                    new_date = input("Enter a new date for the match (dd.mm.yyyy): ") # input validator
                    match_to_change.date = new_date
                    self.__logic_wrapper.update_match(match_to_change)
                    input("Match has been updated, click enter to continue.")
                    
                
                
                
    
    def __choose_team_to_add(self, league):
        while True:
            teams = self.__logic_wrapper.get_all_teams()
            teams_not_in_league = []
            if league.teams == "No teams":
                team_names_in_league = []
            else:
                team_names_in_league = [team.name for team in league.teams]
            c = 1
            for team in teams:
                if team.name in team_names_in_league:
                    pass
                else:
                    teams_not_in_league.append(team)
                    print(f"{c}. {team.name}")
                    c += 1
            if teams_not_in_league == []:
                input("There are no teams to add to the league, click enter to continue.")
                return league
            while True:
                choice = input("Choose a team to add or quit (q): ")
                if choice == "q":
                    return league
                elif choice.isdigit():
                    if 0 < int(choice) < c:
                        team_to_add = teams_not_in_league[int(choice)-1]
                        if league.teams == "No teams":
                            league.teams = [team_to_add]
                        else:
                            league.teams.append(team_to_add)
                        self.__logic_wrapper.update_league(league)
                        again = input(f"{team_to_add.name} has been added to {league.name}, do you want to add another team? (y/n): ")
                        if again == "y":
                            break
                        else:
                            return league
                input("Invalid choice!, click enter to continue")
