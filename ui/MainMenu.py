from ui.AdminPage import AdminPage

class MainMenu:
    

    def __init__(self) -> None:
        print("Welcome")
        print("_"*25)

    def __str__(self) -> str:
        
        return f"{self.menu_output()}{self.input_prompt()}"

    def menu_output(self):
        print("""
    Select an option:

        1. Login with ID
        2. Login as Guest
        3. Admin Login
        'q' to quit""")
        print("_"*25)

    def input_prompt(self):
        selection = input("Enter option: ")
        selection = selection.lower()
        if selection == "q":
            quit
        elif selection == "1":
            ID_input = input("\nEnter ID: ")
        elif selection == '2':
            pass # guest default
        elif selection == "3":
            Admin_login = input("\nEnter admin ID: ")
            #if admin Id is correct, then input password
            Admin_password = input("Password: ")
            #if admin password is correct, run admin option window
            run_admin = AdminPage()
            #clear command?
            print("\n", run_admin)
        else:
            print("Invalid option")


run = MainMenu()
print(run)