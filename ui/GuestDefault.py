
class GuestDefault:

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass

    def options(self):
        print("""
        Select an option:
            1. View Tournament
            2. View Matches
            3. View Clubs, Teams and Players
            'q' to go back to Main Menu""")

    def input_prompt(self):
        option = input("Select an option: ")
