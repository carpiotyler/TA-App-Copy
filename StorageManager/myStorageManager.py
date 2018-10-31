from abc import ABC, abstractmethod


class AbstractStorageManager(ABC):
    # ################################################################################# #
    # The following classes are used for interacting with AbstractStorageManager        #
    # ################################################################################# #
    class Course:

        def __init__(self, str_dept, str_cnum, strarray_sections=[], str_name="", str_description=""):
            self.dept = str_dept
            self.cnum = str_cnum
            self.sections = strarray_sections
            self.name = str_name
            self.description = str_description

    class User:
        def __init(self, str_username, str_password="", str_role=""):
            self.username = str_username
            self.password = str_password
            self.role = str_role

    class Section:
        def __init__(self, str_dept, str_cnum, str_snum):
            self.dept = str_dept
            self.cnum = str_cnum
            self.snum = str_snum

    # ################################################################################# #
    # List of functional storage methods to be implemented by a data system             #
    # ################################################################################# #
    @abstractmethod
    def set_up(self): pass
    # Sets up storage. JSON, Database, whatever. Also creates one user: username=supervisor password=1234 role=supervisor
    # Returns true on successful setup false otherwise

    @abstractmethod
    def insert_course(self, course): pass
    # Inserts a Course to the course list, overwriting if it exists.
    # Does not validate data! Simply makes sure it has received a course object then inserts it to the database.

    @abstractmethod
    def insert_user(self, user): pass
    # Inserts a User to the user list, overwriting if it exists. Does not error check for valid data!
    # Does not validate data! Simply makes sure it has received a user object then inserts it to the database.

    @abstractmethod
    def insert_section(self, section): pass
    # Inserts a Section to the user list, overwriting if it exists. Does not error check for valid data!
    # Does not validate data! Simply makes sure it has received a user object then inserts it to the database.

    @abstractmethod
    def get_course(self, dept, cnum): pass
    # Builds a Course object that has this dept and cnum (plus other data from database) and returns it. None if no entry matches.

    @abstractmethod
    def get_user(self, username): pass
    # Builds a User object that has this username (plus other data from database) and returns it. None if no entry matches

    @abstractmethod
    def get_section(self, dept, cnum, snum): pass
    # Builds a Section object that has this username (plus other data from database) and returns it. None if no entry matches
