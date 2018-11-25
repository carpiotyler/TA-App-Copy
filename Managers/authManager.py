from Managers.myStorageManager import AbstractStorageManager
from Managers.userManager import UserManager as UM
from Domain.user import User


class AuthManager:
    @staticmethod
    def validate(self, command: str) -> bool:
        pass