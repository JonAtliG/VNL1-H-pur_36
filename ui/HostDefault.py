

class HostDefault():

    def __init__(self) -> None:
        pass

    def options(self):
        print("""
    Please select an option:
        1. Create tournament
        2. Change match
        3. View matches played
        4. View teams and players
        'q' to logout.""")
        print("_"*25)

    def input_prompt():
        
        option = input("Select an option: ")

        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == 'q':
            return
        else:
            print("Invalid option")

    def __str__(self) -> str:
        pass
