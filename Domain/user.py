
class User:

    def __init__(self, str_username, str_password="", str_role=""):
        self.username = str_username
        self.password = str_password
        self.role = str_role

    def __str__(self):
        return "username: " + self.username + ", password: " + self.password
