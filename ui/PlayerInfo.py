# import player info
from MainMenu import MainMenu


class PlayerSetup():

    def __init__(self, ID="000000-0000", name="John Smith", address="Street 123", GSM="888-8888", telephone="555-1111", email="smith@email.com", team="Team Name") -> None:
        self.id = ID
        self.name = name
        self.address = address
        self.GSM = GSM
        self.telephone = telephone
        self.email = email
        self.team = team
        print("Player", self.id, "\n")

    def __str__(self) -> str:

        return self.information(), self.options()

    def options(self):
        logout = input("Enter 'q' to logout: ")
        if logout == "q":
            MainMenu()
        else:
            print("Invalid input")

        return logout

    def information(self):
        name = "Full name: " + str(self.name)
        team = "Team: " + str(self.team)
        email = "E-mail: " + str(self.email)
        address = "Address: " + str(self.address)
        telephone = "Telephone: " + str(self.telephone)
        mobile = "Mobile phone: " + str(self.GSM)

        return ("{:>10}\n{:>10}\n{:>10}\n{:>10}\n{:>10}\n{:>10}".format(name, team, email, address, telephone, mobile))


run = PlayerSetup()
print(run)
