from Managers.myStorageManager import AbstractStorageManager as StorageManager
from Managers.abstractManager import ManagerInterface
from TAServer.models import Staff as User
from TAServer.models import DefaultGroup, TAGroup, InsGroup, AdminGroup, SupGroup


class UserManager(ManagerInterface):

    def __init__(self, storage: StorageManager):
        self.storage = storage

    def add(self, fields: dict) -> bool:
        print(fields)
        user = self.storage.get_user(fields.get("username"))

        if user is None:  # user dne
            user = User()
            user.username = "" if fields.get("username") is None else fields.get("username")
            user.address = "" if fields.get("address") is None else fields.get("address"),
            user.phonenum = "" if fields.get("phone_number") is None else fields.get("phone_number")
            user.email = "" if fields.get("email") is None else fields.get("email")
            user.password = "" if fields.get("password") is None else fields.get("password")
            user.role = "" if fields.get("role") is None else fields.get("role")

            if user.role is None or user.role == "default":
                user.groups.add(DefaultGroup())

            elif user.role == "ta":
                user.groups.add(TAGroup())

            elif user.role == "ins":
                user.groups.add(InsGroup())

            elif user.role == "admin":
                user.groups.add(AdminGroup())

            elif user.role == "sup":
                user.groups.add(SupGroup())

            self.storage.insert_user(user)

            return True

        else:  # user exists
            return False

    def view(self, fields) -> str:
        if fields.get("username") is None:  # fetch all users
            users = self.storage.get_user("")
            return '|'.join(map(lambda x: x.__str__(), users))

        else:  # fetch single user
            user = self.storage.get_user(fields.get("username"))
            return "No User Available" if (user is None) else user.__str__()

    def edit(self, fields: dict) -> bool:
        user = self.storage.get_user(fields.get("username"))

        if user is None:  # user dne
            return False

        else:  # found user
            user = User()
            user.username = "" if fields.get("username") is None else fields.get("username")
            user.address = "" if fields.get("address") is None else fields.get("address"),
            user.phonenum = "" if fields.get("phone_number") is None else fields.get("phone_number")
            user.email = "" if fields.get("email") is None else fields.get("email")
            user.password = "" if fields.get("password") is None else fields.get("password")
            user.role = "" if fields.get("role") is None else fields.get("role")

            if user.role is None or user.role == "default":
                user.groups.add(DefaultGroup())

            elif user.role == "ta":
                user.groups.add(TAGroup())

            elif user.role == "ins":
                user.groups.add(InsGroup())

            elif user.role == "admin":
                user.groups.add(AdminGroup())

            elif user.role == "sup":
                user.groups.add(SupGroup())

            self.storage.insert_user(user)
            return True

    def delete(self, fields: dict) -> bool:
        user = self.storage.get_user(fields.get("username"))

        if user is None:  # user dne
            return False
        #
        else:  # found user
            # self.storage.delete_user(user)
            return True
        pass

    @staticmethod
    def reqFields() -> list:
        return ["username", "password", "role"]

    @staticmethod
    def optFields() -> list:
        return ["address", "phone_number", "email"]
