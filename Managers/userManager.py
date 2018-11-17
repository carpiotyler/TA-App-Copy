from Managers.myStorageManager import AbstractStorageManager as StorageManager
from Domain.user import User


class UserManager:

    def __init__(self, storage: StorageManager):
        self.storage = storage

    def add(self, username, password: str = None, role: str = None) -> str:
        user = self.storage.get_user(username)

        if user is not None:  # user exists
            return "User Already Exists"

        else:  # user dne
            _password = "" if password is None else password
            _role = "" if role is None else role
            user = User(username, _password, _role)
            self.storage.insert_user(user)
            return user.__str__()

    def edit(self, username, password: str = None, role: str = None) -> str:
        user = self.storage.get_user(username)

        if user is None:  # user dne
            return "No User Available"

        else:  # found user
            _password = user.password if password is None else password
            _role = user.role if role is None else role
            user = User(username, _password, _role)
            self.storage.insert_user(user)
            return user.__str__()

    def view(self, username: str = None) -> str:

        if username is None:  # fetch all users
            users = self.storage.get_all_users()
            data = map(lambda x: x.__str__(), users)
            return '|'.join(data)

        else:  # fetch single user
            user = self.storage.get_user(username)

            if user is None:  # user dne
                return "No User Available"

            else:  # found user
                return user.__str__()

    def delete(self, username) -> str:

        user = self.storage.get_user(username)

        if user is None:  # user dne
            return "No User Available"

        else:  # found user
            self.storage.delete_user(user)
            return user.__str__()
