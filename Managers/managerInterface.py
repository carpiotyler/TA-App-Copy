# This is my idea for a potential manager interface. Each of the four main functions takes in a dictionary where each
# key value pair is a field and it's value. Each dict must have a non None value for each key returned by reqFields()
# and optFields() just returns optional fields (mainly for correct spelling and capitalization). This is not meant for
# auth manager or databse manager, just course, section, and user.

class ManagerInterface():
    def __init__(self, database: StorageManager):
        pass

    def add(self, fields: dict)->bool:
        pass

    def view(self, fields: dict)->str:
        pass

    def edit(self, fields: dict)->bool:
        pass

    def delete(self, fields: dict)->bool:
        pass

    @static
    def reqFields(self)->list:
        pass

    @static
    def optFields(self)->list:
        pass