from Managers.DjangoStorageManager import DjangoStorageManager
from TAServer.models import User, Section, Course
from django.test import TestCase


class DjangoStorageManagerTests(TestCase):

    # setUp Calls setup function from db. This makes sense as all databases have a hardcoded supervisor to start with,
    # and we test if setup does what it is supposed to later.
    def setUp(self):
        self.storage = DjangoStorageManager()
        self.storage.set_up(self, False)

    # This test just makes sure that after a set_up call (we call this during def setUp in this class) there is a
    # starter supervisor
    def test_set_up(self):
        self.assertEqual(len(User.objects.all()), 1, "After setup, must contain one user!")
        self.assertEqual(len(Section.objects.all()), 1)
        self.assertEqual(len(Course.objects.all()), 1)

        self.assertEqual(len(User.objects.filter(username="supervisor")), 1)
        u = User.objects.get(username="supervisor")
        self.assertIsNotNone(u)
        self.assertEqual(u.password, "123")
        # TODO check role of supervisor

        # Testing database flushing (Overwrite = True
        newuser = User(username= "test", password = "password", role = "")
        newuser.save()
        newcourse = Course(dept="CS", cnum="351")
        newcourse.save()
        newsection = Section(snum = "801", course = newcourse)
        newsection.save()

        u = User.objects.get(username = "test")
        c = Course.objects.get(dept="CS", cnum="351")
        s = Section.objects.get(snum="801", course__dept= "CS", course__cnum="351")
        self.assertIsNotNone(u)
        self.assertIsNotNone(c)
        self.assertIsNotNone(s)

        # Should rebuild database, with none of the following models we had created:
        self.storage.set_up(overwrite=True)
        u = User.objects.get(username="test")
        c = Course.objects.get(dept="CS", cnum="351")
        s = Section.objects.get(snum="801", course__dept="CS", course__cnum="351")
        self.assertIsNone(u)
        self.assertIsNone(c)
        self.assertIsNone(s)

    # NOTE: FOR ALL OTHER TESTS WE ASSUME SETUP WORKS CORRECTLY AND ONLY ONE SUPERUSER IS IN THE DATABASE

    # Testing inserting a Course model
    def test_insert_course(self):
        c = Course(dept = "CS", cnum = "351")
        self.assertFalse(self.storage.insert_course(self, c), "Should return false, not overwriting!")
        retval = Course.objects.get(dept="CS", cnum="351")
        self.assertIsNotNone(retval)
        c.name = "Data Structures and Algorithms"
        self.assertTrue(self.storage.insert_course(c), "Should return true, overwriting!")
        retval = Course.objects.get(dept="CS", cnum="351")
        self.assertIsNotNone(retval)
        self.assertEqual(len(Course.objects.all()), 1, "Should only be 1 course in Courses during this test!")
        self.assertEqual(retval.name, "Data Structures and Algorithms", "Insert didn't properly update the db!")

    # Testing inserting a Section model
    def test_insert_section(self):
        c = Course(dept="CS", cnum="351")
        c.save()
        s = Section(snum="801", course=c)
        self.assertFalse(self.storage.insert_section(self, s), "Should return false, not overwriting!")
        retval = Section.objects.get(snum="801", course__dept="CS", course__cnum="351")
        self.assertIsNotNone(retval)
        s.time = "11:00AM"
        self.assertTrue(self.storage.insert_section(s), "Should return true, overwriting!")
        retval = Section.objects.get(snum="801", course__dept="CS", course__cnum="351")
        self.assertIsNotNone(retval)
        self.assertEqual(len(Section.objects.all()), 1, "Should only be 1 section in Sections during this test!")
        self.assertEqual(retval.time, "11:00AM", "Insert didn't properly update the db!")

    def test_insert_user(self):
        u = User(username="Rock", password="123")
        self.assertFalse(self.storage.insert_user(self, u), "Should return false, not overwriting!")
        retval = User.objects.get(username="Rock")
        self.assertIsNotNone(retval)
        u.password = "password"
        self.assertTrue(self.storage.insert_user(u), "Should return true, overwriting!")
        retval = User.objects.get(username="Rock")
        self.assertIsNotNone(retval)
        self.assertEqual(len(User.objects.all()), 2, "Should only be 2 users in Users during this test!")
        self.assertEqual(retval.password, "password", "Insert didn't properly update the db!")

    def test_get_course(self): pass

    def test_get_courses_by(self): pass

    def test_get_user(self): pass

    def test_get_users_by(self): pass

    def test_get_section(self): pass

    def test_get_sections_by(self): pass

    def test_delete(self): pass
