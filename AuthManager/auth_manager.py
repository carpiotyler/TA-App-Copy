from StorageManager.myStorageManager import AbstractStorageManager as StorageManager
from Domain.user import User


class AuthManager:

    def __init__(self, storage: StorageManager):
        self.storage = storage
        self.users = {}

    def login(self, username: str, password: str) -> (User, str):
        user = self.storage.get_user(username)

        if user is None:  # user dne
            return None, "No User Available"

        elif user.password != password:  # incorrect password
            return None, "Incorrect Credentials"

        else:  # user correctly logged in
            self.users[username] = True
            return user, "Success User Logged In"

    def logout(self, username: str) -> str:
        user = self.storage.get_user(username)

        if user is None:  # user dne
            return "No User Available"

        else:  # logout user
            self.users[username] = False
            return "Success User Logged Out"

    def validate(self, username: str, cmd: str = "", action: str = "") -> bool:
        user = self.storage.get_user(username)

        if user is None:  # user dne
            return False

        else:  # user exists

            return True

            # if user.role == "ta":
            #
            # elif user.role == "supervisor":
            #
            # elif user.role == "instructor":
