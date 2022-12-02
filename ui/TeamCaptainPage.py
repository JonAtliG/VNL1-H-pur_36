from PlayerInfo import PlayerSetup
from MainMenu import MainMenu

class TeamCaptainDefault():
    def __init__(self, ID) -> None:
        self.id = ID

    def __str__(self) -> str:
        pass #on right column, show options, on left show info
        # for line in player setup, print |  line

    def options(self):
        print("""Welcome, ####
        Please select an option:
        1. Record match scores
        'q' to logout.""")

    def input_prompt(self):
        choice = input("Select an option: ")
        #if choice == '1'
        #   open list of matches that have happened
        if choice == 'q':
            MainMenu()
        else:
            print("Invalid option")
