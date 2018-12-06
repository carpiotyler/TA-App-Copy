from Managers.myStorageManager import AbstractStorageManager as StorageManager
from Managers.abstractManager import ManagerInterface
from TAServer.models import Staff as User
from TAServer.models import DefaultGroup, TAGroup, InsGroup, AdminGroup, SupGroup


class UserManager(ManagerInterface):

    def __init__(self, storage: StorageManager):
        self.storage = storage
        self.storage.set_up()

    # This method simply adds a user to the database if they don't exist already.
    # Returns true if a new user was added, returns false otherwise
    def add(self, fields: dict) -> bool:
        # Need username and password to add a user!
        if 'username' not in fields.keys(): return False

        user = self.storage.get_user(fields["username"])
        if user is None:  # user dne!
            user = User()
            user.username = fields["username"]

            # if fields['role'] is either None or "", set fields['role'] to 'default'
            # if fields['role'] exists and is invalid, return false. Otherwise, set role as fields['role']
            if 'role' not in fields.keys() or fields['role'] is None or fields['role'].strip() == "":
                user.role = 'default'
            elif fields['role'] in dict(User.ROLES).values():
                user.role = fields['role']
            else:
                return False

            # Unvalidated fields...
            if 'password' in fields.keys() and fields['password'] is not None and len(
                fields['password'].strip()) > 0: user.password = fields['password']
            if 'phonenum' in fields.keys() and fields['phonenum'] is not None and len(
                fields['phonenum'].strip()) > 0: user.phonenum = fields['phonenum']
            if 'address' in fields.keys() and fields['address'] is not None and len(
                fields['address'].strip()) > 0: user.phonenum = fields['address']
            if 'firstname' in fields.keys() and fields['firstname'] is not None and len(
                fields['firstname'].strip()) > 0: user.phonenum = fields['firstname']
            if 'lastname' in fields.keys() and fields['lastname'] is not None and len(
                fields['lastname'].strip()) > 0: user.phonenum = fields['lastname']
            if 'email' in fields.keys() and fields['email'] is not None and len(
                fields['email'].strip()) > 0: user.phonenum = fields['email']
            if 'bio' in fields.keys() and fields['bio'] is not None and len(
                fields['bio'].strip()) > 0: user.phonenum = fields['bio']

            self.storage.insert_user(user)
            return True

        else:  # user exists
            return False

    # This method returns a string representing all users that match the parameters in "fields"
    # Returns No Users if no matches
    # Will only print out fields given by the input fields dict (for permission obedience)
    # A View that returns a string of multiple users outputs sorted by username
    # String is newlined for each user field, double newlined for every new user displayed

    # NOT FULLY FUNCTIONAL, WE NEED TO BE ABLE TO PASS IN PERMISSIONS TO VIEW CERTAIN FIELDS
    def view(self, fields) -> str:
        retval = ""

        if 'username' in fields.keys() and fields['username'].strip() != "":
            # We have to return just one user's view. ez
            user = self.storage.get_user(fields['username'])
            if user is None:
                retval = 'No Users'
            else:
                retval = "" + user.username + "\n" + "role=" + user.role + "\n\n"

            return retval.lower()
        else:
            # Return mutiple users. (We only support viewing all right now
            users = self.storage.get_users_by()
            users = list(users)
            users.sort(key= lambda User: User.username)
            for user in users:
                retval += user.username + "\n" + "role=" + user.role + "\n\n"
            return retval.lower()

    # This method edits an existing user
    # Returns true if a user existed (And therefore edited), or false if no user existed
    def edit(self, fields: dict) -> bool:
        # Need username to edit a user!
        if 'username' not in fields.keys(): return False

        user = self.storage.get_user(fields["username"])
        if user is not None:  # user exists

            # if fields['role'] is either None or "", set fields['role'] to 'default'
            # if fields['role'] exists and is invalid, return false. Otherwise, set role as fields['role']
            if 'role' not in fields.keys() or fields['role'] is None or fields['role'].strip() == "":
                user.role = 'default'
            elif fields['role'] in dict(User.ROLES).values():
                user.role = fields['role']
            else:
                return False

            # Unvalidated fields...
            if 'password' in fields.keys() and fields['password'] is not None and len(
                fields['password'].strip()) > 0: user.password = fields['password']
            if 'phonenum' in fields.keys() and fields['phonenum'] is not None and len(
                fields['phonenum'].strip()) > 0: user.phonenum = fields['phonenum']
            if 'address' in fields.keys() and fields['address'] is not None and len(
                fields['address'].strip()) > 0: user.phonenum = fields['address']
            if 'firstname' in fields.keys() and fields['firstname'] is not None and len(
                fields['firstname'].strip()) > 0: user.phonenum = fields['firstname']
            if 'lastname' in fields.keys() and fields['lastname'] is not None and len(
                fields['lastname'].strip()) > 0: user.phonenum = fields['lastname']
            if 'email' in fields.keys() and fields['email'] is not None and len(
                fields['email'].strip()) > 0: user.phonenum = fields['email']
            if 'bio' in fields.keys() and fields['bio'] is not None and len(
                fields['bio'].strip()) > 0: user.phonenum = fields['bio']

            self.storage.insert_user(user)
            return True

        else:  # user dne!
            return False

    # Deletes a user if it exists.
    # Returns true if it did delete an existing user, false otherwise
    def delete(self, fields: dict) -> bool:
        if 'username' not in fields.keys(): return False

        user = self.storage.get_user(fields['username'])
        if user is None:
            return False
        else:
            self.storage.delete(user)
            return True

    @staticmethod
    def reqFields() -> list:
        return ["username"]

    @staticmethod
    def optFields() -> list:
        return ["password", "role", "address", "phone_number", "email", "firstname", "lastname", "bio"]
