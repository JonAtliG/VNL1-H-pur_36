
class Admin_Logic():
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
    
    def get_ID(self) -> str:
        return self.data_wrapper.get_admin_id()
    
    def get_Password(self) -> str:
        return self.data_wrapper.get_admin_password()
    
    def verify_ID(self, ID: str) -> bool:
        return self.get_ID() == ID
    
    def verify_Password(self, password: str) -> bool:
        return self.get_Password() == password
