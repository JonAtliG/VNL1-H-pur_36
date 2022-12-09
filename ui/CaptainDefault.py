from model.league import League
from model.team import Team
from model.match import Match
from copy import deepcopy

class CaptainDefault():
    def __init__(self, player, team, logic_connection) -> None:
        self.__logic__wrapper = logic_connection
        self.__player = player
        self.__team = team
        self.__leagues = self.__logic__wrapper.get_leagues_by_team_name(self.__team.name)
        if len(self.__leagues) > 0:
            self.__league = self.__leagues[0]
            self.__date_str = f", Date: {self.__league.start_date} - {self.__league.end_date}"
        else:
            self.__league = "No league"
            self.__date_str = ""
    
    def __change_selected_league(self):
        if len(self.__leagues) > 0:
            c = 1
            for league in self.__leagues:
                print(f"{c}. {league.name}, Date: {league.start_date} - {league.end_date}")
                c += 1
            choice = input("Select a league or go back (q): ")
            if choice == "q":
                return
            elif self.__logic__wrapper.validate_number(choice, c):
                self.__league = self.__leagues[int(choice)-1]
                self.__date_str = f", Date: {self.__league.start_date} - {self.__league.end_date}"
                return
        else:
            input("You are not registed in any leagues, click enter to go back.")
    
    def __set_player_order_of_match(self, match: Match) -> Match:
        second_check = False
        number_strings = ["first", "second", "third", "fourth"]
        players_to_set = []
        team_players = [self.__player]
        [team_players.append(player) for player in self.__team.players]
        available_players = deepcopy(team_players)
        for x, game in enumerate(match.games):
            for i in range(game.player_count):
                c = 1
                for player in available_players:
                    print(f"{c}. {player.name}")
                    c += 1
                if game.player_count == 1:
                    input_msg = f"Choose a player for the {number_strings[x]} 1v1 game or quit (q): "
                elif game.player_count == 2:
                    input_msg = f"Choose the {number_strings[i]} player for the {number_strings[x-4]} 2v2 game or quit (q): "
                else:
                    input_msg = f"Choose the {number_strings[i]} player for the 4v4 game or quit (q): "
                while True:
                    choice = input(input_msg)
                    if self.__logic__wrapper.validate_number(choice, c):
                        players_to_set.append(available_players[int(choice) - 1])
                        available_players.pop(int(choice) - 1)
                        break
                    elif choice == "q":
                        return match
                    else:
                        print("Invalid choice,")
            if x == 3 or x == 5:
                available_players = deepcopy(team_players)
            if match.home_team.captain.nid == self.__player.nid:
                match.games[x].home_players = players_to_set
                players_to_set = []
            else:
                match.games[x].away_players = players_to_set
                players_to_set = []
        self.__logic__wrapper.update_match(match)
        [self.__logic__wrapper.update_game(game) for game in match.games]
        self.__league = self.__logic__wrapper.get_league_by_name(self.__league.name)
        return
                
    
    def __choose_match_to_set_player_order(self):
        unset_matches = []
        for match in self.__league.matches:
            if match.home_team.name == self.__team.name:
                if match.games[0].home_players == "No players":
                    unset_matches.append(match)
            elif match.away_team.name == self.__team.name:
                if match.games[0].away_players == "No players":
                    unset_matches.append(match)
        if len(unset_matches) > 0:
            c = 1
            for match in unset_matches:
                print(f"{c}. {match.home_team.name} vs {match.away_team.name} - {match.date}")
                c += 1
            choice = input("Choose a match to set or go back (q): ")
            if choice == "q":
                return
            elif self.__logic__wrapper.validate_number(choice, c):
                match_to_set = unset_matches[int(choice)-1]
                self.__set_player_order_of_match(match_to_set)
            else:
                input("Invalid choice, click enter to go back.")
        else:
            input("You have no matches with unset player order, click enter to go back.")


    def __set_score_of_match(self):
        #Find matches that don't have scores and do not have no players and you are captain of the hometeam
        unset_matches = []
        for match in self.__league.matches:
            if match.home_team.name == self.__team.name:
                if match.games[0].away_players != "No players" and match.games[0].away_players != "No players" and match.games[0].played == False:
                    unset_matches.append(match)
        
        if len(unset_matches) == 0:
            input("You have no matches with unset scores, click enter to go back.")
            return
        c = 1
        for match in unset_matches:
            print(f"{c}. {match.home_team.name} vs {match.away_team.name} - {match.date}")
            c += 1
        choice = input("Choose a match to set or go back (q): ")
        if choice == "q":
            return
        elif self.__logic__wrapper.validate_number(choice, c):
            match_to_set = unset_matches[int(choice)-1]
            print(f"Match: {match.home_team.name} vs {match.away_team.name}")
            c = 1
            while c <= len(match_to_set.games):
                game = match_to_set.games[c-1]
                print(f"{c}. ({game.home_player_score})\t{', '.join(player.name for player in game.home_players)} |\t{', '.join(player.name for player in game.away_players)} \t({game.away_player_score})")        
                inp = input("Enter the score (home team score - away team score): ")
                try:
                    home, away = inp.split("-")
                    home = int(home.strip())
                    away = int(away.strip())
                    ls = set([home, away])
                    if ls == {0, 2} or ls == {1, 2}:
                        game = self.__logic__wrapper.set_game_score(game, home, away)
                        self.__logic__wrapper.update_game(game)
                        c += 1
                    else:
                        input("Invalid score, click enter to continue.")
                except:
                    input("Invalid score, click enter to continue.")
            return
        else:
            input("Invalid choice, click enter to go back.")
            return
                    



    def options(self):
        print(f"""Captain options - Team: {self.__team.name}
        Current league selected: {self.__league.name}{self.__date_str}
        Please select an option:
        1. Change selected league
        2. Set player order for upcoming matches
        3. Set score for a match
        2. View Teams and Players
        3. See upcoming matches
        'q' to logout.""")

    def input_prompt(self):
        while True:
            self.options()
            choice = input("Select an option: ")
            if choice == '1':
                self.__change_selected_league()
            elif choice == '2':
                self.__choose_match_to_set_player_order()
            elif choice == '3':
                self.__set_score_of_match()
            elif choice == 'q':
                return
            else:
                print("Invalid option")
    