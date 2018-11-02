from StorageManager import myStorageManager
import json, os


class JSONStorageManager(myStorageManager.AbstractStorageManager):

    def __init__(self, str_file_name="database.json"):
        self.file_name = str_file_name

    def set_up(self, overwrite_files=False):
        base_db_json = """
            {
                "courses":[
                
                ],
                
                "users":[
                    {
                        "username":"supervisor",
                        "password":"123",
                        "role":"supervisor"
                    }
                ],
                
                "sections":[
                
                ]
            }
        """
        try:
            file = open(self.file_name)
            file.close()
            if overwrite_files:
                print("Overwriting: " + self.file_name)
                os.remove(self.file_name)
            else:
                return False
        except FileNotFoundError:
            pass
        file = open(self.file_name, "w+")
        file.write(base_db_json)
        file.close()
        return True

    def get_course(self, dept = "", cnum = ""): pass

    def get_section(self, dept, cnum = "", snum = ""): pass

    def get_user(self, username = ""): pass

    def insert_course(self, course): pass

    def insert_section(self, section): pass

    def insert_user(self, user): pass
