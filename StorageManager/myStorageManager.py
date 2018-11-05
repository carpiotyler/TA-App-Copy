from abc import ABC, abstractmethod
from typing import Optional

from Domain.section import Section
from Domain.course import Course
from Domain.user import User


# ################################################################################# #
# List of functional storage methods to be implemented by a data system             #
# ################################################################################# #
# * Note * none of the below methods error check for valid data!


class AbstractStorageManager(ABC):

    @abstractmethod
    def set_up(self): pass
    # Sets up storage. JSON, Database, whatever. Also creates a user: username=supervisor password=1234 role=supervisor
    # Returns true on successful setup false otherwise

# User

    @abstractmethod
    def insert_user(self, user: User): pass
    # Inserts a User to the user list, overwriting if it exists.

    @abstractmethod
    def delete_user(self, user: User): pass
    # Deletes a User from the user list.

    @abstractmethod
    def get_user(self, username) -> Optional[User]: pass
    # Returns a User that has this username (plus other data from database)

    @abstractmethod
    def get_all_users(self) -> [User]: pass
    # Returns a list of User objects.

# Course

    @abstractmethod
    def insert_course(self, course: Course): pass
    # Inserts a Course to the course list, overwriting if it exists.

    @abstractmethod
    def delete_course(self, course: Course): pass
    # Deletes a Course from the course list.

    @abstractmethod
    def get_course(self, dept, cnum) -> Optional[Course]: pass
    # Returns a Course that has this dept and cnum (plus other data from database)

    @abstractmethod
    def get_all_courses(self) -> [Course]: pass
    # Returns a list of Course objects.

    @abstractmethod
    def get_all_courses_by_dept(self, dept) -> [Course]: pass
    # Returns a list of Course objects filtered by dept.

# Section

    @abstractmethod
    def insert_section(self, section: Section): pass
    # Inserts a Section to the section list, overwriting if it exists.

    @abstractmethod
    def delete_section(self, section: Section): pass
    # Deletes a Section from the section list.

    @abstractmethod
    def get_section(self, dept, cnum, snum) -> Optional[Section]: pass
    # Returns a Section that has this username (plus other data from database)

    @abstractmethod
    def get_all_sections(self) -> [Section]: pass
    # Returns a list of Section objects.

    @abstractmethod
    def get_all_sections_by_dept(self, dept) -> [Section]: pass
    # Returns a list of Section objects matching dept.

    @abstractmethod
    def get_all_sections_by_course(self, dept, cnum) -> [Section]: pass
    # Returns a list of Section objects matching dept and course.
