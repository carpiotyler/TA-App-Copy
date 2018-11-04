from StorageManager.myStorageManager import AbstractStorageManager as storage
from Domain.section import Section
from Domain.course import Course
from Domain.user import User
import json, os

class JSONStorageManager(storage):

    def __init__(self, str_file_name="database.json"):
        self.file_name = str_file_name

    def set_up(self, overwrite_files=False):
        # Below is the base json format for an empty database
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
            # This try is testing for if the database file exists or not
            file = open(self.file_name)
            file.close()
            # In the case a file exists, calling setup could be bad (Essentially deleting a database). We check overwrite perms here
            if overwrite_files:
                print("Overwriting: " + self.file_name)
                os.remove(self.file_name)
            else:
                # No database was setup, false returned
                return False
        except FileNotFoundError:
            pass

        # Writing the base JSON to our file database
        file = open(self.file_name, "w+")
        file.write(base_db_json)
        file.close()
        return True

    def get_course(self, dept="", cnum=""):
        # Importing database from json(self.file_name)
        file = open(self.file_name)
        json_database = json.load(file)
        file.close()

        # Please note the difference between dict_course (Python Dict from json) and course_course (database interfacing type)
        if len(dept) == 0 and len(cnum) == 0:
            # Getting all courses and returning as list
            ret_vals = []
            for dict_course in json_database["courses"]:
                course_course = Course(dept, cnum)
                course_course.sections = dict_course["sections"].copy()
                course_course.description = dict_course["description"]
                course_course.name = dict_course["name"]
                ret_vals.append(course_course)
            # This check maintains the practice that if no course exists, return None. Clunky but useful.
            if len(ret_vals) > 0:
                return ret_vals
        elif len(cnum) == 0:
            # Getting all courses that match the dept passed
            ret_vals = []
            for dict_course in json_database["courses"]:
                if dict_course["dept"] == dept:
                    course_course = Course(dept, cnum)
                    course_course.sections = dict_course["sections"].copy()
                    course_course.description = dict_course["description"]
                    course_course.name = dict_course["name"]
                    ret_vals.append(course_course)
            # This check maintains the practice that if no course exists, return None. Clunky but useful.
            if len(ret_vals) > 0:
                return ret_vals
        else:
            # Simply getting one course and returning it
            for dict_course in json_database["courses"]:
                if dict_course["dept"] == dept and dict_course["cnum"] == cnum:
                    course_course = Course(dept, cnum)
                    course_course.sections = dict_course["sections"].copy()
                    course_course.description = dict_course["description"]
                    course_course.name = dict_course["name"]
                    return course_course
        return None

    def get_section(self, dept, cnum, snum):
        # Importing database from json(self.file_name)
        file = open(self.file_name)
        json_database = json.load(file)
        file.close()

        # Getting a section and returning it, or returning none
        for dict_section in json_database["sections"]:
            if dict_section["dept"] == dept and dict_section["cnum"] == cnum and dict_section["snum"] == snum:
                section_section = Section(dept, cnum, snum)
                section_section.instructor = dict_section["instructor"]
                return section_section
        return None

    def get_user(self, username=""):
        # Importing database from json(self.file_name)
        file = open(self.file_name)
        json_database = json.load(file)
        file.close()

        # Getting a user and returning it, or returning none
        for dict_user in json_database["users"]:
            if dict_user["username"] == username:
                user_user = User(username)
                user_user.password = dict_user["password"]
                user_user.role = dict_user["role"]
                return user_user
        return None

    def insert_course(self, course):
        # Inserting a course objects data into JSON
        if isinstance(course, Course):
            file = open(self.file_name)
            json_database = json.load(file)
            file.close()

            # Checking for if the course is in database via dept&cnum, overwriting if one matches
            for dict_course in json_database["courses"]:
                if dict_course["dept"] == course.dept and dict_course["cnum"] == course.cnum:
                    dict_course["sections"] = course.sections.copy()
                    dict_course["description"] = course.description
                    dict_course["name"] = course.name
                    file = open(self.file_name, "w")
                    json.dump(json_database, file, indent=4)
                    file.close()
                    return

            # We make it here if a course doesn't exist yet
            new_dict_course = {'dept': course.dept, 'cnum': course.cnum, 'sections': course.sections.copy(),
                               'name': course.name, 'description': course.description}
            json_database["courses"].append(new_dict_course)
            file = open(self.file_name, "w")
            json.dump(json_database, file, indent=4)
            file.close()
            return

    def insert_section(self, section):
        # Inserting a section objects data into JSON
        if isinstance(section, Section):
            file = open(self.file_name)
            json_database = json.load(file)
            file.close()

            # Checking for if the section is in database via dept&cnum&snum, overwriting if one matches
            for dict_section in json_database["sections"]:
                if dict_section["dept"] == section.dept and dict_section["cnum"] == section.cnum and dict_section[
                    "snum"] == section.snum:
                    dict_section["instructor"] = section.instructor
                    file = open(self.file_name, "w")
                    json.dump(json_database, file, indent=4)
                    file.close()
                    return

            # We make it here if a section doesn't exist yet
            new_dict_section = {'dept': section.dept, 'cnum': section.cnum, 'snum': section.snum,
                                'instructor': section.instructor}
            json_database["sections"].append(new_dict_section)
            file = open(self.file_name, "w")
            json.dump(json_database, file, indent=4)
            file.close()
            return

    def insert_user(self, user):
        # Inserting a user objects data into JSON
        if isinstance(user, User):
            file = open(self.file_name)
            json_database = json.load(file)
            file.close()

            # Checking for if the user is in database via username, overwriting if one matches
            for dict_user in json_database["users"]:
                if dict_user["username"] == user.username:
                    dict_user["password"] = user.password
                    dict_user["role"] = user.role
                    file = open(self.file_name, "w")
                    json.dump(json_database, file, indent=4)
                    file.close()
                    return

            # We make it here if a user doesn't exist yet
            new_dict_user = {'username': user.username, 'password': user.password, 'role': user.role}
            json_database["users"].append(new_dict_user)
            file = open(self.file_name, "w")
            json.dump(json_database, file, indent=4)
            file.close()
            return
