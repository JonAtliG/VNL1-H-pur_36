from ui.DisplayAll import DisplayAll
from logic.logic_wrapper import Logic_Wrapper

class GuestDefault:

    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        self.display_all = DisplayAll(logic_connection)


    def __str__(self) -> str:
        return self.options(), self.input_prompt()

    def options(self):
        print("""
        Select an option:
            1. View League
            2. View Clubs, Teams and Players
            'q' to go back to Main Menu""")

    def input_prompt(self):
        while True:
            self.options()
            option = input("Select an option: ")
            if option == "q":
                return
            elif option == "1":
                #view_tournament_page = ViewTournament(self.logic_wrapper)
                leagues = self.logic_wrapper.get_all_leagues()
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
                        print("1. View finished matches")
                        print("2. View upcoming matches")
                        print('"q". Go back')
                        choice = input("Select an option: ")
                        if choice == "1":
                            DisplayAll.display_finished_matches(league)
                        elif choice == "2":
                            DisplayAll.display_unfinished_matches(league)
                        elif choice == "q":
                            return
                        else:
                            input("Invalid option, click enter to continue.")
                else:
                    input("Invalid option, click enter to continue.")



            elif option == "2":
                self.display_all.view_all()
            else:
                input("Invalid option, click enter to continue.")
