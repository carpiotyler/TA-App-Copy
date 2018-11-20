

class User:

    def __init__(
         self,
         username: str="",
         password: str="",
         role: str="",
         address: str="",
         phone_number: str="",
         email: str=""
    ):
        self.username = username
        self.password = password
        self.role = role
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return "username: {0}, password: {1}, role: {2}, address: {3}, phone_number: {4}, email: {5}"\
            .format(self.username, self.password, self.role, self.address, self.phone_number, self.email)
