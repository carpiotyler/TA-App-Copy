
class User:

    def __init__(self, str_username, str_password="", str_role=""):
        self.username = str_username
        self.password = str_password
        self.role = str_role

    def __str__(self):
        return "\nUser: {\n\tusername: " + self.username + "\n\tpassword: " + self.password + "\n}"
