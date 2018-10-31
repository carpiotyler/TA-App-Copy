import unittest


class AuthManager:

    def __index__(self):
        print("AuthManager: init")

    def login(self, username: str, password: str):
        print("AuthManager: login "+username+" "+password)

    def logout(self, username: str):
        print("AuthManager: logout "+username)


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.fixture = AuthManager()

    def tearDown(self):
        del self.fixture

    def test_login(self):
        pass

    def test_logout(self):
        pass

