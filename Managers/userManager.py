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
    def add(self, fields: dict):
        # Need username and password to add a user!
        if 'username' not in fields.keys(): return False, "Please fill out username"

        user = self.storage.get_user(fields["username"])
        if user is None:  # user dne!
            user = User()
            user.username = fields["username"]

            # if fields['role'] is either None or "", set fields['role'] to 'Default'
            # if fields['role'] exists and is invalid, return false. Otherwise, set role as fields['role']
            if 'role' not in fields.keys() or fields['role'] is None or fields['role'].strip() == "":
                user.role = dict(User.ROLES)['D']
            elif fields['role'] in dict(User.ROLES).values():
                user.role = fields['role']
            else:
                return False, "Role invalid!"

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
            return True, ""

        else:  # user exists
            return False, "User Exists!"

    # Returns a list of user dicts that match the parameters.
    # Will ALWAYS return list, if getting a single user, ret[0] will be the user's field dict
    # Currently supports this logic -> sorting by username(Unique) -> sorting by role(all with a role) -> returning all
    # Multiple values sorted alphabetically by username

    def view(self, fields) -> [dict]:
        retVal = []

        if 'username' in fields.keys() and fields['username'].strip() != "":
            # We have to return just one user's view. ez
            user = self.storage.get_user(fields['username'])
            if user is None:
                # No users case
                retVal = []
            else:
                # Put all users fields into a dict
                retFields = {}
                retFields['username'] = fields['username']
                retFields['password'] =  user.password
                retFields['firstname'] = user.firstname
                retFields['lastname'] = user.lastname
                retFields['bio'] = user.bio
                retFields['email'] = user.email
                retFields['role'] = user.role
                retFields['phonenum'] = user.phonenum
                retFields['address'] = user.address
                retVal.append(retFields)
            return retVal
        else:
            # Return mutiple users. (We only support viewing all right now
            matchingusers = []
            if 'role' in fields.keys() and fields['role'].strip() != "":
                # Return all users by a role
                matchingusers = self.storage.get_users_by(fields['role'])
            else:
                # Return all users
                matchingusers = self.storage.get_users_by()
            for user in matchingusers:
                retFields = {}
                retFields['username'] = user.username
                retFields['password'] = user.password
                retFields['firstname'] = user.firstname
                retFields['lastname'] = user.lastname
                retFields['bio'] = user.bio
                retFields['email'] = user.email
                retFields['role'] = user.role
                retFields['phonenum'] = user.phonenum
                retFields['address'] = user.address
                retVal.append(retFields)

            # Sort by username
            retVal.sort(key= lambda k: k['username'])
            return retVal

    # This method edits an existing user
    # Returns true if a user existed (And therefore edited), or false if no user existed
    def edit(self, fields: dict):
        # Need username to edit a user!
        if 'username' not in fields.keys(): return False, "Please fill out username"

        user = self.storage.get_user(fields["username"])
        if user is not None:  # user exists

            # if fields['role'] is either None or "", set fields['role'] to 'default'
            # if fields['role'] exists and is invalid, return false. Otherwise, set role as fields['role']
            if 'role' not in fields.keys() or fields['role'] is None or fields['role'].strip() == "":
                user.role = 'default'
            elif fields['role'] in dict(User.ROLES).values():
                user.role = fields['role']
            else:
                return False, "Role Invalid!"

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
            return True, ""

        else:  # user dne!
            return False, "User doesn't exist!"

    # Deletes a user if it exists.
    # Returns true if it did delete an existing user, false otherwise
    def delete(self, fields: dict) -> bool:
        if 'username' not in fields.keys(): return False, "Please fill out username"

        user = self.storage.get_user(fields['username'])
        if user is None:
            return False, "No user to delete!"
        else:
            self.storage.delete(user)
            return True, ""

    @staticmethod
    def reqFields() -> list:
        return ["username"]

    @staticmethod
    def optFields() -> list:
        return ["password", "role", "address", "phone_number", "email", "firstname", "lastname", "bio"]
