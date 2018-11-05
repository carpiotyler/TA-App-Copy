from myStorageManager import AbstractStorageManager as StorageManager


class User:

    def __init__(self, str_username, str_password="", str_role=""):
        self.username = str_username
        self.password = str_password
        self.role = str_role

    def __str__(self):
        return "username: " + self.username + ", password: " + self.password


class UserManager:

    def __init__(self, storage: StorageManager):
        pass

    def add(self, username, password: str=None, role: str=None) -> str:
        pass

    def edit(self, username, password: str=None, role: str=None) -> str:
        pass

    def view(self, username: str=None) -> str:
        pass

    def delete(self, username) -> str:
        pass
