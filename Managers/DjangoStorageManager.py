# Helper class for dealing with django's database
# See myStorageManager Interface for full documentation on method behaviors
from Managers.myStorageManager import AbstractStorageManager
from TAServer.models import Course, Section, User


class DjangoStorageManager(AbstractStorageManager):

    def set_up(self, overwrite=False): pass

    def insert_course(self, course: Course)->bool: pass

    def insert_section(self, section: Section)->bool: pass

    def insert_user(self, user: User)->bool: pass

    def get_users_by(self)->[User]: pass

    def get_user(self, username)->User: pass

    def get_course(self, dept, cnum)->Course: pass

    def get_courses_by(self, dept, cnum)->[Course]: pass

    def get_section(self, dept, cnum, snum)->[Section]: pass

    def get_sections_by(self, dept, cnum, snum)->[Section]: pass

    def delete(self, to_delete)->bool: pass