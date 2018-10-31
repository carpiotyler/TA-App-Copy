import unittest


class User:

    def __init__(self, username, password="", role=""):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return "\n User: {\nusername: "+self.username+"\npassword: "+self.password+"}"


class UserManager:

    def __index__(self):
        print("UserManager: init")

    def add(self, user: User):
        print("UserManager: add "+user.__str__())

    def delete(self, user: User):
        print("UserManager: delete "+user.__str__())

    def edit(self, user: User):
        print("UserManager: edit "+user.__str__())

    def view(self, user: User):
        print("UserManager: view "+user.__str__())


class UserTest(unittest.TestCase):

    def setUp(self):
        self.fixture = UserManager()

    def tearDown(self):
        del self.fixture

    def test_user_add(self):
        pass

    def test_delete_user(self):
        pass

    def test_edit_user(self):
        pass

    def test_view_user(self):
        pass


