from data.CSV_Handler import CSV_Handler

class Admin_Data():
    def __init__(self):
        self.file_name = "data/files/admin_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def get_password(self) -> str:
        return self.__CSV_Handler.get_data_by_line_index(1)[1]
    
    def get_ID(self) -> str:
        return self.__CSV_Handler.get_data_by_line_index(1)[0]

