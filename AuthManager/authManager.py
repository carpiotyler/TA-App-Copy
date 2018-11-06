from StorageManager.myStorageManager import AbstractStorageManager
from Domain.user import User


class AuthManager:

    def __init__(self, storage: AbstractStorageManager):
        self.storage = storage
        self.allowed = {}

    def login(self, username: str, password: str) -> (User, str):
        user = self.storage.get_user(username)

        if user is None:  # user dne
            return None, "No User Available"

        elif user.password != password:  # incorrect password
            return None, "Incorrect Credentials"

        elif self.allowed.__contains__(username) \
                and self.allowed[username] is True:  # already logged in
            return None, "User Already Logged In"

        else:  # user correctly logged in
            self.allowed[username] = True
            return user, "Success User Logged In"

    def logout(self, username: str) -> str:
        user = self.storage.get_user(username)

        if user is None:  # user dne
            return "No User Available"

        elif not self.allowed.__contains__(username) \
                or self.allowed[username] is False:  # already logged out
            return "User Already Logged Out"

        else:  # logout user
            self.allowed[username] = False
            return "Success User Logged Out"

    def validate(self, username: str, cmd: str = "", action: str = "") -> bool:
        user = self.storage.get_user(username)

        if user is None:  # user dne
            return False

        elif not self.allowed.__contains__(username):  # user not logged in
            return False

        else:  # user exists

            role = user.role.lower()

            if role == "ta":

                if cmd == "Course":
                    return action == "view"

                elif cmd == "Section":
                    return action == "view"

                elif cmd == "User":
                    return action == "view"
