class CaptainDefault():
    def __init__(self, player, team, logic_connection) -> None:
        self.__logic_connection = logic_connection
        self.__player = player
        self.__team = team

    def __str__(self) -> str:
        pass #on right column, show options, on left show info
        # for line in player setup, print |  line

    def options(self):
        print(f"""Captain options - Team: {self.__team.name}
        Please select an option:
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
