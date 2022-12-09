from ui.Display_Information import Display_Information
from model.league import League
from model.match import Match
import datetime

class HostDefault():
    def __init__(self, hostid, logic_connection) -> None:
        '''Constructor for HostDefault class.'''
        self.__logic_wrapper = logic_connection
        self.__display_information = Display_Information(logic_connection)
        self.__host = self.__logic_wrapper.get_host_by_id(hostid)
    
    def input_prompt(self):
        '''Prompts the user to enter an option.'''
        while True:
                self.__options()
                option = input("Select an option: ")
                if option == "q":
                    return
                elif option == "1":
                    print("_"*30)
                    self.__create_league()
                elif option == "2":
                    print("_"*30)
                    self.__league_options()
                elif option == "3":
                    self.__display_information.display_leagues()
                else:
                    input("Invalid option, click enter to continue.")

    
    def __options(self):
        '''Displays the options for the HostDefault class.'''
        print("""
    Please select an option:
        1. Create League
        2. Choose League  
        3. View leagues  
        'q' to logout.
              """)
    
    def __create_league(self):
        '''Creates a league.'''
        league = League()
        leagues = self.__logic_wrapper.get_all_leagues()
        #while loops to validate input
        while True:

            name = input("Enter a name for the league: ")
            if name not in [league.name for league in leagues] and self.__logic_wrapper.validate_name(name):
                break
            elif not self.__logic_wrapper.validate_name(name):
                input("Invalid name, click enter to continue.")
            else:
                input("League name already exists, click enter to continue.")
        league.name = name
        while True:
            league.start_date = input("Enter start date for the league (dd.mm.yyyy): ")
            if self.__logic_wrapper.validate_date(league.start_date) and datetime.datetime.strptime(league.start_date, "%d.%m.%Y") >= datetime.datetime.now():
                break
            else:
                input("Invalid date, click enter to continue.")
        while True:
            league.end_date = input("Enter end date for the league (dd.mm.yyyy): ")
            if self.__logic_wrapper.validate_date(league.end_date) and datetime.datetime.strptime(league.end_date, "%d.%m.%Y") > datetime.datetime.strptime(league.start_date, "%d.%m.%Y"):
                break
            else:
                input("Invalid date, click enter to continue.")
        if self.__host.league_names == "No leagues":
            self.__host.league_names = []
        self.__host.league_names.append(league.name)
        self.__logic_wrapper.add_league(league)
        self.__logic_wrapper.update_host(self.__host)
    
    def __league_options(self) -> None:
        '''Displays the options for the league options menu.'''
        while True:
            if self.__host.league_names == "No leagues":
                input("You have no leagues, click enter to continue.")
                return
            leagues = [self.__logic_wrapper.get_league_by_name(name) for name in self.__host.league_names]
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
                    while True:
                        print("_"*30)
                        print(f"League: {league.name}")
                        print("1. Plan an upcoming match")
                        print("2. Change time of an upcoming match")
                        print("3. Change score of a finished game")
                        print("4. Add teams to league")
                        print('"q". Go back')
                        choice = input("Select an option: ")
                        if choice == "1":
                            league = self.__create_match(league)
                        elif choice == "2":
                            self.__change_time_of_upcoming_match(league)
                        elif choice == "3":
                            self.change_score_of_finished_game(league)
                        elif choice == "4":
                            league = self.__choose_team_to_add(league)
                        elif choice == "q":
                            return
                        else:
                            input("Invalid option, click enter to continue.")
            else:
                input("Invalid option, click enter to continue.")
    
    def change_score_of_finished_game(self, league: League):
        '''Changes the score of a finished game.'''
        if league.matches == "No matches":
            input("There are no matches in the league, click enter to continue.")
            return
        else:
            finished_matches = []
            for match in league.matches:
                if match.games[0].played:
                    finished_matches.append(match)
            if len(finished_matches) == 0:
                input("There are no finished matches in the league, click enter to continue.")
                return
            else:
                c = 1
                for match in finished_matches:
                    print(f"{c}. {match.home_team.name} vs {match.away_team.name}")
                    c += 1
                print("_"*30)
                #get the match to change the score of
                while True:
                    choice = input("Choose a match to change the score of or quit (q): ")
                    if self.__logic_wrapper.validate_number(choice, c):
                        match = finished_matches[int(choice)-1]
                        #get each game in the match
                        while True:
                            print(f"Match: {match.home_team.name} vs {match.away_team.name}")
                            games = match.games
                            c = 1
                            for game in games:
                                print(f"{c}. ({game.home_player_score})\t{', '.join(player.name for player in game.home_players)} |\t{', '.join(player.name for player in game.away_players)} \t({game.away_player_score})")
                                c += 1
                            print("_"*30)
                            choice = input("Choose a game to change the score of or quit (q): ")
                            if self.__logic_wrapper.validate_number(choice, c):
                                game = games[int(choice)-1]
                                while True:
                                    inp = input("Enter the new score (home team score - away team score): ")
                                    if inp == "q":
                                        return
                                    try:
                                        home, away = inp.split("-")
                                        home = int(home.strip())
                                        away = int(away.strip())
                                        ls = set([home, away])
                                        if ls == {0, 2} or ls == {1, 2}:
                                            game = self.__logic_wrapper.set_game_score(game, home, away)
                                            self.__logic_wrapper.update_game(game)
                                            return
                                    except:
                                        pass
                                    input("Invalid score, click enter to continue.")
                            elif choice == "q":
                                return
                            else:
                                input("Invalid option, click enter to continue.")
                                return
                    elif choice == "q":
                        return


    def __create_match(self, league: League) -> League:
        '''Creates a match.'''
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
            #get the home team
            while True:
                choice = input("Choose a home team for the match or quit (q): ")
                if self.__logic_wrapper.validate_number(choice, c):
                    match.home_team = league.teams[int(choice)-1]
                    c = 1
                    possible_away_teams = []
                    for team in league.teams:
                        if team.name == match.home_team.name:
                            pass
                        else:
                            print(f"{c}. {team.name}")
                            possible_away_teams.append(team)
                            c += 1
                    #get the away team
                    while True:
                        choice = input("Choose an away team for the match or quit (q): ")
                        if self.__logic_wrapper.validate_number(choice, c):
                            match.away_team = possible_away_teams[int(choice)-1]
                            #get the date of the match
                            while True:
                                date = input("Enter a date for the match (dd.mm.yyyy) or quit (q): ")
                                if self.__logic_wrapper.validate_date(date, league.start_date, league.end_date):
                                    match.date = date
                                    break
                                elif date == "q":
                                    return league
                                else:
                                    print("Invalid date.")
                            match = self.__logic_wrapper.give_match_games(match)
                            if league.matches == "No matches":
                                league.matches = [match]
                            else:
                                league.matches.append(match)
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
    
    def __change_time_of_upcoming_match(self, league: League):
        '''Changes the time of an upcoming match.'''
        if league.matches == "No matches":
            input("League has no matches, click enter to continue.")
        else:
            upcoming_matches = []
            for match in league.matches:
                if not match.games[0].played:
                    upcoming_matches.append(match)
            if len(upcoming_matches) > 0:
                c = 1
                for match in upcoming_matches:
                    print(f"{c}. {match.home_team.name} vs {match.away_team.name} - Date: {match.date}")
                    c += 1
                choice = input("Choose a match to change its date or quit (q): ")
                while True:
                    if choice == "q":
                        return
                    elif self.__logic_wrapper.validate_number(choice, c):
                        match_to_change = upcoming_matches[int(choice)-1]
                        while True:
                            new_date = input("Enter a new date for the match (dd.mm.yyyy) or quit (q): ")
                            if self.__logic_wrapper.validate_date(new_date, league.start_date, league.end_date):
                                match_to_change.date = new_date
                                self.__logic_wrapper.update_match(match_to_change)
                                input("Match has been updated, click enter to continue.")
                                return
                            elif new_date != "q":
                                print("Invalid date.")
                            else:
                                return
                    else:
                        input("Invalid choice, click enter to continue.")
            else:
                input("The league has no upcoming matches, click enter to continue.")
                return
                
    def __choose_team_to_add(self, league):
        '''Chooses a team to add to a league.'''
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
            #get the team to add
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
