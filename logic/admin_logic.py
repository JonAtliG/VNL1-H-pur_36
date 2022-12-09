
class Admin_Logic():
    def __init__(self, data_connection) -> None:
        '''Constructor for Admin_Logic class.'''
        self.data_wrapper = data_connection
    
    def get_ID(self) -> str:
        '''Returns the ID of the admin.'''
        return self.data_wrapper.get_admin_id()
    
    def get_Password(self) -> str:
        '''Returns the password of the admin.'''
        return self.data_wrapper.get_admin_password()
    
    def verify_ID(self, ID: str) -> bool:
        '''Returns True if the ID is correct, False otherwise.'''
        return self.get_ID() == ID
    
    def verify_Password(self, password: str) -> bool:
        '''Returns True if the password is correct, False otherwise.'''
        return self.get_Password() == password
