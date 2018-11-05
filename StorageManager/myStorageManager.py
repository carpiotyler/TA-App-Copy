from abc import ABC, abstractmethod
from Domain.section import Section
from Domain.course import Course
from Domain.user import User

class AbstractStorageManager(ABC):

    # ################################################################################# #
    # List of functional storage methods to be implemented by a data system             #
    # ################################################################################# #
    @abstractmethod
    def set_up(self): pass
    # Sets up storage. JSON, Database, whatever. Also creates one user: username=supervisor password=1234 role=supervisor
    # Returns true on successful setup false otherwise

    @abstractmethod
    def insert_course(self, course: Course): pass
    # Inserts a Course to the course list, overwriting if it exists.
    # Does not validate data! Simply makes sure it has received a course object then inserts it to the database.

    @abstractmethod
    def insert_user(self, user: User): pass
    # Inserts a User to the user list, overwriting if it exists. Does not error check for valid data!
    # Does not validate data! Simply makes sure it has received a user object then inserts it to the database.

    @abstractmethod
    def insert_section(self, section: Section): pass
    # Inserts a Section to the user list, overwriting if it exists. Does not error check for valid data!
    # Does not validate data! Simply makes sure it has received a section object then inserts it to the database.

    @abstractmethod
    def get_all_courses(self) -> [Course]: pass
    # Returns a list of Course objects.

    @abstractmethod
    def get_all_courses_by_dept(self, dept) -> [Course]: pass
    # Returns a list of Course objects filtered by dept.

    @abstractmethod
    def get_course(self, dept, cnum) -> Course: pass
    # Builds a Course object that has this dept and cnum (plus other data from database) and returns it. None if no entry matches.

    @abstractmethod
    def get_all_users(self) -> [User]: pass
    # Returns a list of User objects.

    @abstractmethod
    def get_user(self, username) -> User: pass
    # Builds a User object that has this username (plus other data from database) and returns it. None if no entry matches

    @abstractmethod
    def get_all_sections(self) -> [Section]: pass
    # Returns a list of Section objects.

    @abstractmethod
    def get_section(self, dept, cnum, snum) -> [Section]: pass
    # Builds a Section object that has this username (plus other data from database) and returns it. None if no entry matches

    # (NOT IMPLEMENTED/MAY NEVER BE NECESSARY) Returns a list of Section Objects that match (dept, cnum) if snum is not specified (All sections of a course). Returns a list that
    # (NOT IMPLEMENTED/MAY NEVER BE NECESSARY) Matches dept only if (cnum, snum) are not specified. Returns all sections if cnum, dept, snum are all blank.