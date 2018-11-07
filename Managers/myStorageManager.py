from abc import ABC, abstractmethod
from Domain.course import Course
from Domain.section import Section
from Domain.user import User


class AbstractStorageManager(ABC):
    # Type conversions so legacy code works with Domain folder
    class Course(Course):
        pass

    class Section(Section):
        pass

    class User(User):
        pass

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
    # Does not validate data! Simply makes sure it has received a section object then inserts it to the database.

    @abstractmethod
    def get_course(self, dept, cnum): pass
    # Builds a Course object that has this dept and cnum (plus other data from database) and returns it. None if no entry matches.
    # Returns a list of Course Objects that match dept if cnum is not specified. If dept and cnum are both blank, returns all courses as a list.

    @abstractmethod
    def get_user(self, username): pass
    # Builds a User object that has this username (plus other data from database) and returns it. None if no entry matches
    # Returns a list of User objects if username is not specified.

    @abstractmethod
    def get_section(self, dept, cnum, snum): pass
    # Builds a Section object that has this username (plus other data from database) and returns it. None if no entry matches

    # (NOT IMPLEMENTED/MAY NEVER BE NECESSARY) Returns a list of Section Objects that match (dept, cnum) if snum is not specified (All sections of a course). Returns a list that
    # (NOT IMPLEMENTED/MAY NEVER BE NECESSARY) Matches dept only if (cnum, snum) are not specified. Returns all sections if cnum, dept, snum are all blank.
