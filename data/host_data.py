from data.CSV_Handler import CSV_Handler

class Host_Data():
    def __init__(self) -> None:
        self.__file_name = "data/files/host_data.csv"
        self.__CSV_Handler = CSV_Handler(self.__file_name)
    
    def __get_all_host_data(self):
        return self.__CSV_Handler.get_all_data()
    
    def verify_id(self, id):
        host_data = self.__get_all_host_data()
        for host_id in host_data:
            if host_id == id:
                return True
        return False
    
    def get_league_names_by_id(self, id):
        return self.__CSV_Handler.get_data_by_data(id, 0)[2].strip("\n").split(",")
    
    def get_host_name_by_id(self, id):
        return self.__CSV_Handler.get_data_by_data(id, 0)
    
    def add_host(self, id):
        self.__CSV_Handler.add_line(id)