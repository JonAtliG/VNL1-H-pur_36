class Admin_Data():
    def __init__(self):
        self.file_name = "data/files/admin_data.csv"
    
    def get_password(self):
        with open(self.file_name, "r") as csv:
            for i in csv:
                password = i.split(";")[1]
                return password

    def get_ID(self):
        with open(self.file_name, "r") as csv:
            for i in csv:
                id = i.split(";")[0]
                return id