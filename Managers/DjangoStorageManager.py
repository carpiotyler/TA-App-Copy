# Helper class for dealing with django's database
# See myStorageManager Interface for full documentation on method behaviors
from Managers.myStorageManager import AbstractStorageManager
from TAServer.models import Course, Section, User


class DjangoStorageManager(AbstractStorageManager):

    def set_up(self, overwrite=False)->bool:
        if len(Section.objects.all()) > 0 or len(User.objects.all()) > 0 or len(Course.objects.all()) > 0:
            # Database isn't empty!
            if not overwrite:
                return False
            else:
                for section in Section.objects.all():
                    section.delete()
                for user in User.objects.all():
                    user.delete()
                for course in Course.objects.all():
                    course.delete()
        sup = User(username="supervisor", password="123")
        self.insert_user(sup)
        return True

    def insert_course(self, course: Course)->bool: pass

    def insert_section(self, section: Section)->bool: pass

    def insert_user(self, user: User)->bool:
        existinguser = self.get_user(user.username)
        # Checking if user already exists
        if existinguser != None:
            # overwrite case
            return True

        user.save()
        return False


    def get_users_by(self)->[User]: pass

    def get_user(self, username: str)->User: pass

    def get_course(self, dept: str, cnum: str)->Course: pass

    def get_courses_by(self, dept: str, cnum: str)->[Course]: pass

    def get_section(self, dept: str, cnum: str, snum: str)->[Section]: pass

    def get_sections_by(self, dept: str, cnum: str, snum: str)->[Section]: pass

    def delete(self, to_delete)->bool: pass
