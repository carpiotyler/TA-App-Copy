from Managers.DjangoStorageManager import DjangoStorageManager
from TAServer.models import User, Section, Course
from django.test import TestCase
import unittest

class DjangoStorageManagerTests(TestCase):

    # setUp Calls setup function from db. This makes sense as all databases have a hardcoded supervisor to start with,
    # and we test if setup does what it is supposed to later.
    def setUp(self):
        self.storage = DjangoStorageManager()
        self.storage.set_up(overwrite=False)

    # This test just makes sure that after a set_up call (we call this during def setUp in this class) there is a
    # starter supervisor
    def test_set_up(self):
        self.assertEqual(User.objects.all().count(), 1, "After setup, must contain one user!")
        self.assertEqual(Section.objects.all().count(), 0)
        self.assertEqual(Course.objects.all().count(), 0)

        self.assertEqual(User.objects.filter(username="supervisor").count(), 1)
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

    # Testing insert_course
    def test_insert_course(self):
        c = Course(dept = "CS", cnum = "351")
        self.assertFalse(self.storage.insert_course(self, c), "Should return false, not overwriting!")
        retval = Course.objects.get(dept="CS", cnum="351")
        self.assertIsNotNone(retval)
        c.name = "Data Structures and Algorithms"
        self.assertTrue(self.storage.insert_course(c), "Should return true, overwriting!")
        retval = Course.objects.get(dept="CS", cnum="351")
        self.assertIsNotNone(retval)
        self.assertEqual(Course.objects.all().count(), 1, "Should only be 1 course in Courses during this test!")
        self.assertEqual(retval.name, "Data Structures and Algorithms", "Insert didn't properly update the db!")

    # Testing insert_section
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

    #Testing insert_user
    def test_insert_user(self):
        # TODO check for role
        u = User(username="Rock", password="123")
        self.assertFalse(self.storage.insert_user(self, u), "Should return false, not overwriting!")
        retval = User.objects.get(username="Rock")
        self.assertIsNotNone(retval)
        u.password = "password"
        self.assertTrue(self.storage.insert_user(u), "Should return true, overwriting!")
        retval = User.objects.get(username="Rock")
        self.assertIsNotNone(retval)
        self.assertEqual(User.objects.all().count(), 2, "Should only be 2 users in Users during this test!")
        self.assertEqual(retval.password, "password", "Insert didn't properly update the db!")

    # Testing get_course
    def test_get_course(self):
        c = Course(dept="CS", cnum="351", name="Data Structures and Algorithms")
        c.save()
        retval = self.storage.get_course(dept="CS", cnum="351")
        self.assertIsNotNone(retval)
        self.assertIsInstance(retval, Course)
        self.assertEqual(retval.name, "Data Structures and Algorithms")

    # Testing get_courses_by (filter version for searches)
    def test_get_courses_by(self):
        c1 = Course(dept="CS", cnum="351")
        c2 = Course(dept="CS", cnum="240")
        c3 = Course(dept="MATH", cnum="240")
        c1.save()
        c2.save()
        c3.save()

        # Testing getting course by providing dept and cnum (should be unique - 1 course!)
        retval = self.storage.get_courses_by(self, dept="MATH", cnum="240")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 1)
        self.assertEqual(list.__contains__(self, c3))

        # Testing getting course by providing dept
        retval = self.storage.get_courses_by(self, dept="CS")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 2)
        self.assertEqual(list.__contains__(self, c1))
        self.assertEqual(list.__contains__(self, c2))

        # Testing getting course by providing cnum
        retval = self.storage.get_courses_by(self, cnum="240")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 2)
        self.assertEqual(list.__contains__(self, c2))
        self.assertEqual(list.__contains__(self, c3))

        # Testing getting course by providing nothing (all)
        retval = self.storage.get_courses_by(self)
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 3)
        self.assertEqual(list.__contains__(self, c1))
        self.assertEqual(list.__contains__(self, c2))
        self.assertEqual(list.__contains__(self, c3))

    # Testing get_user
    def test_get_user(self):
        # TODO Verify Roles
        u = User(username="Rock", password="123")
        u.save()
        retval = self.storage.get_user("Rock")
        self.assertIsNotNone(retval)
        self.assertIsInstance(retval, User)
        self.assertEqual(retval.password, "123")

    # Testing get_users_by (Filter version for searches)
    def test_get_users_by(self):
        # TODO Verify Roles
        u1 = User(username="Rock", password="123")
        u2 = User(username="Boyland", password="Andrew")
        u1.save()
        u2.save()

        # Testing getting user by providing username(should be unique - 1 user!)
        retval = self.storage.get_users_by(username="Rock")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 1)
        self.assertEqual(list.__contains__(self, u1))

        # Testing getting course by providing nothing (all users)
        retval = self.storage.get_users_by(self)
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 2)
        self.assertEqual(list.__contains__(self, u1))
        self.assertEqual(list.__contains__(self, u2))

    # Testing get_section
    def test_get_section(self):
        c = Course(dept="CS", cnum="351", name="Data Structures and Algorithms")
        c.save()
        s = Section(snum="801", course=c, time="11:00AM")
        s.save()
        retval = self.storage.get_section(snum="801",dept="CS", cnum="351")
        self.assertIsNotNone(retval)
        self.assertIsInstance(retval, Section)
        self.assertEqual(retval.time, "11:00AM")
        self.assertEqual(retval.course.cnum, "351")
        self.assertEqual(retval.course.dept, "CS")

    # Testing get_sections_by (filter version for searches)
    def test_get_sections_by(self):
        c1 = Course(dept="CS", cnum="351")
        c2 = Course(dept="CS", cnum="337")
        c1.save()
        c2.save()

        s1 = Section(snum="801", course=c1)
        s2 = Section(snum="801", course=c2)
        s3 = Section(snum ="802", course=c1)
        s1.save()
        s2.save()
        s3.save()

        # Testing getting sections by providing snum, dept, and cnum (should be unique - 1 section!)
        retval = self.storage.get_sections_by(self, dept="CS", cnum="351", snum="801")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 1)
        self.assertEqual(list.__contains__(self, s1))

        # Testing getting sections by providing dept
        retval = self.storage.get_sections_by(self, dept="CS")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 3)
        self.assertEqual(list.__contains__(self, s1))
        self.assertEqual(list.__contains__(self, s2))
        self.assertEqual(list.__contains__(self, s3))

        # Testing getting sections by providing cnum
        retval = self.storage.get_sections_by(self, cnum="351")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 2)
        self.assertEqual(list.__contains__(self, s1))
        self.assertEqual(list.__contains__(self, s3))

        # Testing getting section by providing dept and cnum
        retval = self.storage.get_sections_by(self, dept="CS", cnum="351")
        self.assertIsInstance(retval, list)
        self.assertEqual(len(list.count()), 2)
        self.assertEqual(list.__contains__(self, s1))
        self.assertEqual(list.__contains__(self, s3))

        # Testing getting sections by providing dept and snum
        retval = self.storage.get_sections_by(self, dept="CS", snum="801")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 2)
        self.assertEqual(list.__contains__(self, s1))
        self.assertEqual(list.__contains__(self, s2))

        # Testing getting sections by providing cnum and snum
        retval = self.storage.get_sections_by(self, cnum="351", snum="801")
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 1)
        self.assertEqual(list.__contains__(self, s1))

        # Testing getting sections by providing nothing (all)
        retval = self.storage.get_sections_by(self)
        self.assertIsInstance(retval, list)
        self.assertEqual(list.count(), 3)
        self.assertEqual(list.__contains__(self, s1))
        self.assertEqual(list.__contains__(self, s2))
        self.assertEqual(list.__contains__(self, s3))

    def test_delete(self):
        c = Course(dept="CS", cnum="351")
        s = Section(snum="801", course=c)
        u = User(user="Rock", password="123")

        # None of these objects are in the database, so nothing should be deleted
        self.assertFalse(self.storage.delete(c))
        self.assertFalse(self.storage.delete(s))
        self.assertFalse(self.storage.delete(u))

        c.save()
        s.save()
        u.save()
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(Section.objects.all().count(), 1)
        self.assertEqual(User.objects.all().count(), 2)

        # Deleting objects here
        self.assertTrue(self.storage.delete(s))
        self.assertTrue(self.storage.delete(c))
        self.assertTrue(self.storage.delete(u))
        self.assertEqual(Course.objects.all().count(), 0)
        self.assertEqual(Section.objects.all().count(), 0)
        self.assertEqual(User.objects.all().count(), 1)

        c.save()
        s.save()
        u.save()
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(Section.objects.all().count(), 1)
        self.assertEqual(User.objects.all().count(), 2)

        # Testing course -> section cascade delete
        self.assertTrue(self.storage.delete(c))
        self.assertEqual(Course.objects.all().count(), 0)
        self.assertEqual(Section.objects.all().count(), 0)
        self.assertEqual(User.objects.all().count(), 2)
