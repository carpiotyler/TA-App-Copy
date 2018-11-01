class User:

    def __init__(self, username, password="", role=""):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return "%s:\n\t%s" % (self.username, self.role)


class UserManager:
    def __index__(self):
        pass

    def add(self, user: User):
        pass

    def delete(self, user: User):
        pass

    def edit(self, user: User):
        pass

    def view(self, user: User):
        pass
