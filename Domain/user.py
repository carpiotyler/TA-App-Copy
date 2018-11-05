
class User:

    def __init__(self, username: str="", password: str="", str_role: str=""):
        self.username = username
        self.password = password
        self.role = str_role

    def __str__(self):
        return "username: {0}, password: {1}, role: {2}".format(self.username, self.password, self.role)

