from user_manager import User


class AuthManager:
    def __index__(self):
        pass

    def login(self, username: str, password: str):
        return User(username)

    def logout(self, username: str):
        pass

    def auth(self, user: User):
        return True # Placeholder
