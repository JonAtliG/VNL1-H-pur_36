from model.host import Host

class Host_logic():
    def __init__(self, data_connection) -> None:
        self.__data_wrapper = data_connection
    
    def __make_host_object_from_data(self, data):
        host = Host()
        host.id = data[0]
        host.name = data[1]
        host.league_names = [name for name in data[2].split(",")]
        return host
    
    def verify_id(self, id):
        return self.__data_wrapper.verify_host_id(id)
    
    def get_host_by_league_name(self, name):
        return self.__make_host_object_from_data(self.__data_wrapper.get_host_data_by_league_name(name))
    
    def get_host_by_id(self, id):
        return self.__make_host_object_from_data(self.__data_wrapper.get_host_data_by_id(id))
    
    def add_host(self, host):
        self.__data_wrapper.add_host(host)
    
    def update_host(self, host):
        self.__data_wrapper.update_host(host)