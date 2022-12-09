from logic.logic_wrapper import Logic_Wrapper
from ui.AdminPage import AdminPage
from ui.GuestDefault import GuestDefault
from ui.PlayerDefault import PlayerDefault
from ui.HostDefault import HostDefault

class MainMenu:
    
    
    def __init__(self) -> None:
        '''Constructor for MainMenu class.'''
        self.logic_wrapper = Logic_Wrapper()

    #def __str__(self) -> str:
    #    
    #    return f"{self.menu_output()}{self.input_prompt()}"

    def menu_output(self):
        '''Displays the menu for the MainMenu class.'''
        print("_"*30)
        print("          Welcome!!!")
        print("_"*30)
        print("""
    Select an option:

        1. Login with ID
        2. Login as Guest
        3. Admin Login
        4. Host Login
        'q' to quit
        """)

    def input_prompt(self):
        '''Prompts the user to enter an option.'''
        while True:
            self.menu_output()
            selection = input("Enter option: ")
            selection = selection.lower()
            if selection == "q":
                return
                
            elif selection == "1":
                print("_"*30)
                ID_input = input("\nEnter ID: ")
                if self.logic_wrapper.is_valid_player_id(ID_input):
                    player = PlayerDefault(self.logic_wrapper, ID_input)
                    player.input_prompt()
                else:
                    input("Invalid ID, click enter to continue. ")
                    
            elif selection == '2':
                print("_"*30)
                guest_default_page = GuestDefault(self.logic_wrapper)
                guest_default_page.input_prompt()
            elif selection == "3":
                print("_"*30)
                Admin_login = input("\nEnter admin ID: ")
                if self.logic_wrapper.verify_admin_id(Admin_login):
                    Admin_password = input("Password: ")
                    if self.logic_wrapper.verify_admin_password(Admin_password):
                        admin_page = AdminPage(self.logic_wrapper)
                        admin_page.input_prompt()
                        continue
                    else:
                        input("Incorrect password, click enter to continue")
                else:
                    input("Incorrect ID, click enter to continue")
            elif selection == "4":
                print("_"*30)
                self.host_login()
            else:
                print("Invalid option")

    def host_login(self):
        '''Prompts the user to enter a host ID.'''
        ID_input = input("\nEnter host ID: ")
        if self.logic_wrapper.verify_host_id(ID_input):
            host = HostDefault(ID_input, self.logic_wrapper)
            host.input_prompt()
        else:
            input("Host ID does not exist, click enter to continue.")
            return
