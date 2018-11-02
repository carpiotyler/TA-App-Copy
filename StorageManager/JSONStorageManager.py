from StorageManager.myStorageManager import AbstractStorageManager as storage

import json, os


class JSONStorageManager(storage):

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

    def get_course(self, dept = "", cnum = ""):
        # Importing database from json(self.file_name)
        file = open(self.file_name)
        json_database = json.load(file)
        file.close()

        if len(dept) == 0 and len(cnum) == 0:
            # Getting all courses and returning as list
            ret_vals = []
            for dict_course in json_database["courses"]:
                course_course = storage.Course(dept, cnum)
                course_course.sections = dict_course["sections"].copy()
                course_course.description = dict_course["description"]
                course_course.name = dict_course["name"]
                ret_vals.append(course_course)
            if len(ret_vals) > 0:
                return ret_vals
        elif len(cnum) == 0:
            # Getting all courses that match the dept passed
            ret_vals = []
            for dict_course in json_database["courses"]:
                if dict_course["dept"] == dept:
                    course_course = storage.Course(dept, cnum)
                    course_course.sections = dict_course["sections"].copy()
                    course_course.description = dict_course["description"]
                    course_course.name = dict_course["name"]
                    ret_vals.append(course_course)
            if len(ret_vals) > 0:
                return ret_vals
        else:
            # Simply getting one course and returning it
            for dict_course in json_database["courses"]:
                if dict_course["dept"] == dept and dict_course["cnum"] == cnum:
                    course_course = storage.Course(dept, cnum)
                    course_course.sections = dict_course["sections"].copy()
                    course_course.description = dict_course["description"]
                    course_course.name = dict_course["name"]
                    return course_course
        return None

    def get_section(self, dept, cnum = "", snum = ""): pass

    def get_user(self, username = ""): pass

    def insert_course(self, course): pass

    def insert_section(self, section): pass

    def insert_user(self, user): pass
