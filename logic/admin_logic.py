
class Admin_Logic():
    
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
    
    def get_ID(self):
        return self.data_wrapper.get_admin_id()
    
    def get_Password(self):
        return self.data_wrapper.get_admin_password()
    
    def verify_ID(self, ID):
        return self.get_ID() == ID
    
    def verify_Password(self, password):
        return self.get_Password() == password
