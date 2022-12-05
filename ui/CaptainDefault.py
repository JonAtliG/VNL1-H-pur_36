from ui.PlayerDefault import PlayerDefault

class CaptainDefault():
    def __init__(self, ID) -> None:
        self.id = ID

    def __str__(self) -> str:
        pass #on right column, show options, on left show info
        # for line in player setup, print |  line

    def options(self):
        print("""Welcome, ####
        Please select an option:
        1. Record match scores
        2. View Teams and Players
        3. See upcoming matches
        'q' to logout.""")

    def input_prompt(self):
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
