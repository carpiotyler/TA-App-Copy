from StorageManager.myStorageManager import AbstractStorageManager
from Domain.user import User


class UserManager:

    def __init__(self, storage: AbstractStorageManager):
        self.storage = storage
        print("UserManager: init")

    def add(self, user: User):
        print("UserManager: add "+user.__str__())
        self.storage.insert_user(user)

    def delete(self, user: User):
        print("UserManager: delete "+user.__str__())


    def edit(self, user: User):
        print("UserManager: edit "+user.__str__())


    def view(self, user: User):
        print("UserManager: view "+user.__str__())
        self.storage.get_user(user.username)


