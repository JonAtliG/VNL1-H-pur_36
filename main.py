from ui.MainMenu import MainMenu

#Main function for the program.
try:
    mainmenu = MainMenu()
    mainmenu.input_prompt()
except:
    print("An unexpected error occured, please try again.")
