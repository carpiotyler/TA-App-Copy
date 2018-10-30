from StorageManager import myStorageManager
import json


class JSONStorageManager(myStorageManager.AbstractStorageManager):

    def __init__(self, str_filename="default.json"):
        self.file_name = str_filename

    def set_up(self): pass

    def get_course(self, dept, cnum): pass

    def get_section(self, dept, cnum, snum): pass

    def get_user(self, username): pass

    def insert_course(self, course): pass

    def insert_section(self, section): pass

    def insert_user(self, user): pass


database = JSONStorageManager("test.json")

print(database.Course.cnum)
