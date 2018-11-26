# Helper class for dealing with django's database
# See myStorageManager Interface for full documentation on method behaviors
from Managers.myStorageManager import AbstractStorageManager
from TAServer.models import Course, Section, Staff as User

class DjangoStorageManager(AbstractStorageManager):

    @staticmethod
    def set_up(overwrite=False)->bool:
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
        DjangoStorageManager.insert_user(sup)
        return True

    @staticmethod
    def insert_course(course: Course)->bool: pass

    @staticmethod
    def insert_section(section: Section)->bool: pass

    @staticmethod
    def insert_user(user: User)->bool:
        existinguser = DjangoStorageManager.get_user(user.username)
        # Checking if user already exists
        if existinguser != None:
            # overwrite case
            return True

        user.save()
        return False

    @staticmethod
    def get_users_by()->[User]: pass

    @staticmethod
    def get_user(username: str)->User:
        return User.objects.filter(username=username).first()

    @staticmethod
    def get_course(dept: str, cnum: str)->Course: pass

    @staticmethod
    def get_courses_by(dept: str, cnum: str)->[Course]: pass

    @staticmethod
    def get_section(dept: str, cnum: str, snum: str)->[Section]: pass

    @staticmethod
    def get_sections_by(dept: str, cnum: str, snum: str)->[Section]: pass

    @staticmethod
    def delete(to_delete)->bool: pass
