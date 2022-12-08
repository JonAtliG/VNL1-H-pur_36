from data.CSV_Handler import CSV_Handler
from model.host import Host

class Host_Data():
    def __init__(self) -> None:
        self.__file_name = "data/files/host_data.csv"
        self.__CSV_Handler = CSV_Handler(self.__file_name)
    
    def __make_host_data_from_object(self, host: Host) -> str:
        host_data = f"{host.id};"
        host_data += f"{host.name};"
        if host.league_names == "No leagues":
            host_data += "No leagues"
        else:
            host_data += ",".join(host.league_names)
        return host_data
    
    def verify_id(self, id):
        try:
            self.__CSV_Handler.get_data_by_data(id, 0)
            return True
        except:
            return False

    def get_host_data_by_league_name(self, name):
        return self.__CSV_Handler.get_data_by_data_in_data(name, 2)
    
    def get_host_data_by_id(self, id):
        return self.__CSV_Handler.get_data_by_data(id, 0)
    
    def add_host(self, host: Host):
        data = self.__make_host_data_from_object(host)
        self.__CSV_Handler.add_line(data)
        
    def update_host(self, host: Host):
        index = self.__CSV_Handler.get_line_index_by_data(host.id, 0)
        data = self.__make_host_data_from_object(host)
        self.__CSV_Handler.replace_line(index, data)