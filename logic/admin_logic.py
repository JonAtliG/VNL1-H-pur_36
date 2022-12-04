
class Admin_Logic():
    
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
    
    def get_ID(self):
        return self.data_wrapper.get_admin_id()
    
    def get_Password(self):
        return self.data_wrapper.get_admin_password()
    
    def verify_ID(self, ID):
        if self.get_ID() == ID:
            return True
        else:
            return False
    
    def verify_Password(self, password):
        if self.get_Password() == password:
            return True
        else:
            return False
