from abc import ABC, abstractmethod


class AbstractStorageManager(ABC):
    # ################################################################################# #
    # The following classes are used for interacting with AbstractStorageManager        #
    # ################################################################################# #
    class Course:
        dept = ""
        cnum = ""
        sections = []
        name = ""
        description = ""

    class User:
        username = ""
        password = ""
        role = ""

    class Section:
        dept = ""
        cnum = ""
        snum = ""

    # ################################################################################# #
    # List of functional storage methods to be implemented by a data system             #
    # ################################################################################# #
    @abstractmethod
    def set_up(self): pass
    # Sets up storage. JSON, Database, whatever. Also creates one user: username=supervisor password=1234 role=supervisor

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
