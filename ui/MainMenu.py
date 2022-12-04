from logic.logic_wrapper import Logic_Wrapper
from ui.AdminPage import AdminPage

class MainMenu:
    
    
    def __init__(self) -> None:
        self.logic_wrapper = Logic_Wrapper()

    #def __str__(self) -> str:
    #    
    #    return f"{self.menu_output()}{self.input_prompt()}"

    def menu_output(self):
        print("Welcome")
        print("_"*30)
        print("""
    Select an option:

        1. Login with ID
        2. Login as Guest
        3. Admin Login
        'q' to quit""")
        print("_"*30)

    def input_prompt(self):
        while True:
            self.menu_output()
            selection = input("Enter option: ")
            selection = selection.lower()
            if selection == "q":
                quit()
            elif selection == "1":
                ID_input = input("\nEnter ID: ")
            elif selection == '2':
                pass # guest default
            elif selection == "3":
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

            else:
                print("Invalid option")


run = MainMenu()
print(run)