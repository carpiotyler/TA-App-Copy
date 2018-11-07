from user_manager import UserManager as UM
from sectionManager import sectionManager as SM
from courseManager import CourseManager as CM
from auth_manager import AuthManager as AM
from JSONStorageManager import JSONStorageManager as JSM

# This is the command parser class, used to bridge the gap between the CLI and our managers so the managers are able to
# work with the website version (or whatever is next). This class has only static methods and only one public function,
# parse. Each function has one mandatory field command which contains the string of the command to be executed and two
# optional fields. One for a user which is not needed in all cases but if a user is not provided then the parser assumes
# that one is not logged in and defaults to that permissions level. The other field is for testing this class and if set
# to true does not interact with any API or manager but instead returns the method it would've with the parameters it
# would've used. This is the best way I can figure out how to test this without turning this into an integration test
# and validating that the parser works based on the APIs or the database. At this point and time (sprint 1) if the
# testing field is true, then the user field does not matter (because checking the auth would become partly integration
# testing with the auth manager). Hopefully this does not break any scrum/agile stuff. The testing field could be a huge
# security flaw if left in but for now it's my best solution.


class CommandParser:
    # These two data sets contain the all the commands and their description. The first array is useful for testing if
    # the parse function has been passed a valid command and the descriptions are useful for help and telling the user
    # when they messed up a command call.
    commandList = ['login', 'logout', 'course', 'section', 'user', 'help', 'exit']
    descriptionList = {'login': "Placeholder description for login",
                       'logout': "Placeholder description for logout",
                       'course': "Placeholder description for course",
                       'section': "Placeholder description for section",
                       'user': "Placeholder description for user",
                       'help': "Placeholder description for help",
                       'exit': "Placeholder description for exit"}

    # This dictionary contains the a set of key values pairs where the key is the command name and the value is the
    # class the handles all that. It contains department because im still not exactly clear how we're going to deal with
    # the department command without a department manager (or if we even still need a department command). This is
    # useful for formatting the strings to return when testing.
    namesdict = {"user": "UserManager",
                 "course": "CourseManager",
                 "section": "sectionManager",
                 "department": "DepartmentManger"}

    # The only field is an optional set to True if the class is being unit tested. If set to true, parse will return the
    # command calls and the params as a string.
    def __init__(self, uting: bool = False):
        self.user = None
        self.uting = uting
        self.commandList = CommandParser.commandList

        self.authmgr = AM()
        self.usermgr = UM(JSM())
        self.coursemgr = CM()
        self.sectionmgr = SM()

    def currentUser(self):
        return self.user

    # The only public function of this class that will either call other helper methods to parse any of the larger
    # commands or if the command is simple it parses it itself. Case does not matter for the command, fields won't
    # lose their case.
    def parse(self, command: str)->str:
        cmdarr = command.split(" ")
        cmdarr[0] = cmdarr[0].lower()

        if(len(cmdarr) == 0 or not (cmdarr[0] in CommandParser.commandList)):
            return "Command not found"

        elif(cmdarr[0] == 'course'):
            return self.parseCourse(command)

        elif(cmdarr[0] == 'section'):
            return self.parseSection(command)

        elif(cmdarr[0] == 'user'):
            return self.parseUser(command)

        elif(cmdarr[0] == 'exit'):
            exit() # This just stops the whole program but whatever

        elif(cmdarr[0] == 'login'):
            if(len(cmdarr) < 3):
                return "Not enough fields to login"

            self.user = self.authmgr.login(cmdarr[1], cmdarr[2])

            return "Success"

        elif(cmdarr[0] == 'logout'):
            if(self.user is None):
                return "Not currently logged in"

            self.authmgr.logout(self.user.username)

            self.user = None

            return "Logged out"

        elif(cmdarr[0] == 'help'):
            if(cmdarr[1].lower() in CommandParser.descriptionList):
                return CommandParser.descriptionList[cmdarr[1].lower()]
            return "Could not find that command"

        else:
            return "Invalid Command"

    # A helper method to just be used inside this class to parse one of the major commands, course. This also checks
    # auth to insure that the user has perms to do what they're trying to do.
    def parseCourse(self, command:str)->str:
        reqFields = ['dept', 'cnum']
        optFields = ['snum', 'ins']

        cmdarr = command.split(" ")
        if(len(cmdarr) < 2):
            return "Invalid use"

        command = cmdarr[0].lower()
        action = cmdarr[1].lower()
        fields = CommandParser.fieldsToDict(cmdarr[2:])

        if(not self.uting and not self.authmgr.isAuthorized(self.user, command, action)):
            return "Not authorized"

        if(action == 'view' and len(fields) == 0):
            if(self.uting):
                return "%s.view()" % CommandParser.namesdict['course']
            return self.coursemgr.view()

        for f in fields:
            if f not in reqFields and f not in optFields:
                return "Unknown field: %s" % f

        for f in reqFields: # If a required field is not in the given fields
            if f not in fields:
                return "Missing field: %s" % f

        for f in optFields: # Replacing optional fields with a None so that function can be called without error
            if f not in fields:
                fields[f] = None

        if(not command == 'course'):
            return "Something went wrong!"

        if(self.uting):
            return '%s.%s(dept="%s", cnum="%s", section="%s", ins="%s")'%(CommandParser.namesdict['course'], action, fields['dept'], fields['cnum'], fields['snum'], fields['ins'])

        if(action == 'add'):
            return self.coursemgr.add(dept=fields['dept'], cnum=fields['cnum'], section=fields['snum'], instr=fields['ins'])

        elif(action == 'edit'):
            return self.coursemgr.edit(dept=fields['dept'], cnum=fields['cnum'], section=fields['snum'], instr=fields['ins'])

        elif(action == 'view'):
            return self.coursemgr.view(dept=fields['dept'], cnum=fields['cnum'], section=fields['snum'], instr=fields['ins'])

        elif(action == 'delete' or action == 'remove'):
            return self.coursemgr.delete(dept=fields['dept'], cnum=fields['cnum'], section=fields['snum'], instr=fields['ins'])

        else:
            return "Unknown action: %s" % action

    # A helper method to just be used inside this class to parse one of the major commands, section. This also checks
    # auth to insure that the user has perms to do what they're trying to do.
    def parseSection(self, command:str)->str:
        reqFields = ['dept', 'cnum', 'snum']
        optFields = ['ins']

        cmdarr = command.split(" ")
        if(len(cmdarr) < 2):
            return "Invalid use"

        command = cmdarr[0].lower()
        action = cmdarr[1].lower()
        fields = CommandParser.fieldsToDict(cmdarr[2:])

        if(not self.uting and not self.authmgr.isAuthorized(self.user, command, action)):
            return "Not authorized"

        if(action == 'view' and len(fields) == 0):
            if(self.uting):
                return "%s.view()" % CommandParser.namesdict['section']
            return self.sectionmgr.view()

        for f in fields:
            if f not in reqFields and f not in optFields:
                return "Unknown field: %s" % f

        for f in reqFields: # If a required field is not in the given fields
            if f not in fields:
                return "Missing field: %s" % f

        for f in optFields: # Replacing optional fields with a None so that function can be called without error
            if f not in fields:
                fields[f] = None

        if(not command == 'section'):
            return "Something went wrong!"

        if(self.uting):
            return '%s.%s(dept="%s", cnum="%s", snum="%s", ins="%s")' % (CommandParser.namesdict['section'], action, fields['dept'], fields['cnum'], fields['snum'], fields['ins'])

        if(action == 'add'):
            return self.sectionmgr.add(dept=fields['dept'], cnum=fields['cnum'], snum=fields['snum'], ins=fields['ins'])

        elif(action == 'edit'):
            return self.sectionmgr.edit(dept=fields['dept'], cnum=fields['cnum'], snum=fields['snum'], ins=fields['ins'])

        elif(action == 'view'):
            return self.sectionmgr.view(dept=fields['dept'], cnum=fields['cnum'], snum=fields['snum'], ins=fields['ins'])

        elif(action == 'delete' or action == 'remove'):
            return self.sectionmgr.delete(dept=fields['dept'], cnum=fields['cnum'], snum=fields['snum'], ins=fields['ins'])

        else:
            return "Unknown action: %s" % action

    # A helper method to just be used inside this class to parse one of the major commands, user. This also checks
    # auth to insure that the user has perms to do what they're trying to do.
    def parseUser(self, command:str)->str:
        reqFields = ['user']
        optFields = ['pass', 'role']

        cmdarr = command.split(" ")
        if(len(cmdarr) < 2):
            return "Invalid use"

        command = cmdarr[0].lower()
        action = cmdarr[1].lower()
        fields = CommandParser.fieldsToDict(cmdarr[2:])

        if (not self.uting and not self.authmgr.isAuthorized(self.user, command, action)):
            return "Not authorized"

        if(action == 'view' and len(fields) == 0):
            if(self.uting):
                return '%s.view()' % CommandParser.namesdict['user']
            return self.usermgr.view()

        for f in fields:
            if f not in reqFields and f not in optFields:
                return "Unknown field: %s" % f

        for f in reqFields: # If a required field is not in the given fields
            if f not in fields:
                return "Missing field: %s" % f

        for f in optFields: # Replacing optional fields with a None so that function can be called without error
            if f not in fields:
                fields[f] = None

        if(not command == 'user'):
            return "Something went wrong!"

        if(action == 'add'):
            if(self.uting):
                return '%s.add("%s", password="%s", role="%s")' % (CommandParser.namesdict['user'], fields['user'], fields['pass'], fields['role'])
            return self.usermgr.add(fields['user'], password=fields['pass'], role=fields['role'])

        elif(action == 'edit'):
            if(self.uting):
                return '%s.edit("%s", password="%s", role="%s")' % (CommandParser.namesdict['user'], fields['user'], fields['pass'], fields['role'])
            return self.usermgr.edit(fields['user'], password=fields['pass'], role=fields['role'])

        elif(action == 'view'):
            if(self.uting):
                return '%s.view("%s")' % (CommandParser.namesdict['user'], fields['user'])
            return self.usermgr.view(fields['user'])

        elif(action == 'delete' or action == 'remove'):
            if(self.uting):
                return '%s.delete("%s")' % (CommandParser.namesdict['user'], fields['user'])
            return self.usermgr.delete(fields['user'])

        else:
            return "Unknown action: %s" % action

    # Another helper method to convert to help convert the fields to be passed to the managers. If the given list would
    # have two different values for one key only the last one will be saved. If the given array contains a code it must
    # come first
    @staticmethod
    def fieldsToDict(arr: list, delimiter: str = '=')->dict:
        rtr = {}

        if(len(arr) == 0):
            return rtr

        if(("code%s"%delimiter) in arr[0]):
            rtr = CommandParser.codeToDict(arr[0])

        for entry in arr:
            if(not ("code%s"%delimiter) in entry):
                kvpair = entry.split(delimiter)

                if(len(kvpair) > 1):
                    rtr[kvpair[0]] = kvpair[1]

        return rtr

    # Hopefully the last helper method, used to convert a code to a dictionary of it's parts
    # EX: "code=CS-351-601" -> {'dept': 'CS', 'cnum': '351', 'snum': '601'}
    @staticmethod
    def codeToDict(code: str)->dict:
        cArr = code.split("-")
        rtr = {'dept': cArr[0][5:]} # the [5:] removes the code= part

        if(len(cArr) > 1):
            rtr['cnum'] = cArr[1]

        if(len(cArr) > 2):
            rtr['snum'] = cArr[2]

        return rtr
