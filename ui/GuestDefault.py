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
            1. View League
            2. View Clubs, Teams and Players
            'q' to logout
            """)

    def input_prompt(self):
        while True:
            self.options()
            option = input("Select an option: ")
            if option == "q":
                return
            elif option == "1":
                leagues = self.logic_wrapper.get_all_leagues()
                c = 1
                for league in leagues:
                    print(f"{c}. {league.name}")
                    c += 1
                print(f"'q' to go back: ")
                league_choice = input("Select a league: ")
                if league_choice == "q":
                    return
                elif league_choice.isdigit():
                    if 1 <= int(league_choice) < c:
                        league = leagues[int(league_choice) - 1]
                        host = self.logic_wrapper.get_host_by_league_name(league.name)
                        print(f"League: {league.name} ({host.name}, phonenumber: {league.phone_number})")
                        print("1. View finished matches")
                        print("2. View upcoming matches")
                        print("3. View leaderboard")
                        print('"q". Go back')
                        choice = input("Select an option: ")
                        if choice == "1":
                            self.display_all.display_finished_matches(league)
                        elif choice == "2":
                            self.display_all.display_unfinished_matches(league)
                        elif choice == "3":
                            self.display_all.display_leaderboard(league)
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