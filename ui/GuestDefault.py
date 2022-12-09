from ui.Display_Information import Display_Information

class GuestDefault:

    def __init__(self, logic_connection) -> None:
        '''Constructor for GuestDefault class.'''
        self.__logic_wrapper = logic_connection
        self.__display_information = Display_Information(logic_connection)


    def __str__(self) -> str:
        '''Returns the GuestDefault class as a string.'''
        return self.options(), self.input_prompt()

    def options(self):
        '''Displays the options for the GuestDefault class.'''
        print("""
        Select an option:
            1. View Leagues
            2. View Clubs, Teams and Players
            'q' Logout
            """)

    def input_prompt(self):
        '''Prompts the user to enter an option.'''
        while True:
            self.options()
            option = input("Enter option: ")
            if option == "q":
                return
            elif option == "1":
                self.__display_information.display_leagues()
            elif option == "2":
                self.__display_information.view_all()
            else:
                input("Invalid option, click enter to continue.")