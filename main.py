from ui.MainMenu import MainMenu

mainmenu = MainMenu()
try:
    mainmenu.input_prompt()
except:
    print("Something went wrong, please try again.")