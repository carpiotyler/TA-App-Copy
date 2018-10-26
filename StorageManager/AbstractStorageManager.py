from abc import ABC, abstractmethod
from enum import Enum


# The following Enums are used for interacting with arrays returned by AbstractStorageManager
class Course(Enum):
    DEPT = 0
    CNUM = 1
    SECTIONS = 2
    NAME = 3
    DESCRIPTION = 4


class User(Enum):
    USERNAME = 0
    PASSWORD = 1
    ROLE = 2

class AbstractStorageManager(ABC):
    """
    List of functional storage methods to be implemented by a data system
    """


    @abstractmethod
    def set_up(self): pass
    # Sets up storage

    @abstractmethod
    def add_course(self, dept, cnum): pass
    # Adds a course to the course list

    @abstractmethod
    def add_user(self, username, password): pass
    # Adds a user to the user list

    @abstractmethod
    def get_course(self, dept, cnum): pass
    # returns an array representing the course requested, or None if nothing

    @abstractmethod
    def get_user(self, username): pass
    # Returns an array representing the user requested, or None if nothing
