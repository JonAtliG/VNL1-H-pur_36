from model.host import Host

class Host_logic():
    def __init__(self, data_connection) -> None:
        '''Constructor for Host_Logic class.'''
        self.__data_wrapper = data_connection
    
    def __make_host_object_from_data(self, data: list) -> Host:
        '''Creates host object from the data and returns it'''
        host = Host()
        host.id = data[0]
        host.name = data[1]
        if data[2] == "No leagues":
            host.league_names = data[2]
        else:
            host.league_names = [name for name in data[2].split(",")]
        return host
    
    def verify_id(self, id):
        '''Forwards id to data_wrapper, returns true if the ID exists in the file'''
        return self.__data_wrapper.verify_host_id(id)
    
    def get_host_by_league_name(self, name: str) -> Host:
        '''Returns the host object, for the given name'''
        return self.__make_host_object_from_data(self.__data_wrapper.get_host_data_by_league_name(name))
    
    def get_host_by_id(self, id: str) -> Host:
        '''Returns the host object, for the given ID'''
        return self.__make_host_object_from_data(self.__data_wrapper.get_host_data_by_id(id))
    
    def add_host(self, host: Host) -> None:
        '''Forwards host object to data_wrapper, to add to the file'''
        self.__data_wrapper.add_host(host)
    
    def update_host(self, host: Host) -> None:
        '''Forwards host object to data_wrapper, to add to the file'''
        self.__data_wrapper.update_host(host)
