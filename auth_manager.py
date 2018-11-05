from user_manager import User


class AuthManager:
    def __index__(self):
        pass

    def login(self, username: str, password: str)->User:
        return User(username)

    def logout(self, username: str):
        pass

    def isAuthorized(self, user: User, command: str, action: str)->bool:
        return True # Just so I can test everything