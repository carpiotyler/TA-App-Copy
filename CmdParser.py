from Managers.userManager import UserManager as UM
from Managers.sectionManager import mySectionManager as SM
from Managers.courseManager import CourseManager as CM
from Managers.authManager import AuthManager as AM
from Managers.JSONStorageManager import JSONStorageManager as JSM

# This class used to bridge the gap between the CLI and the managers so it would be easy to transfer to django but
# because of how we use django in this sprint, we still need this parser. This class does not need anything to be
# initialized but has option fields for all the managers for testing. Refer /Tests/unit_tests/parserTests.py for further
# explanation. This class only has one public function: parse which just requires the command to parse and returns a
# string ready to be displayed. Weather that string will contain HTML or not, we'll have to see.


class CommandParser:

    descriptionList = {'login': "Placeholder description for login",
                       'logout': "Placeholder description for logout",
                       'course': "Placeholder description for course",
                       'section': "Placeholder description for section",
                       'user': "Placeholder description for user",
                       'help': "Placeholder description for help",
                       'exit': "Placeholder description for exit"}

    def __init__(self, mySM:SM = None, myUM:UM = None, myCM:CM = None, myAM:AM = None):
        pass

    # Parses the course command
    def course(self, command: str)->str:
        pass

    # Parses the section command
    def section(self, command: str)->str:
        pass

    # Parses the user command
    def user(self, command: str)->str:
        pass

    # Parses the login command
    def login(self, command: str)->str:
        pass

    # Parses the logout command
    def logout(self, command: str)->str:
        pass

    # Parses the help command
    def help(self, command: str)->str:
        pass

    # Parses the exit command
    def exit(self, command: str)->str:
        pass

    # This needs to be here to see all the above functions as handles
    commandList = [login, logout, course, section, user, help, exit]

    # Finds the right function to call and calls it
    # This is currently just a proof of concept to show how we could implement the way rock did it in the lab without
    # having to call ever command and check what they return and ahve to check in each command function if they're the
    # right one.
    def parse(self, command: str) -> str:
        split = command.split(" ")
        command = split[0].lower()

        for cmd in self.commandList:
            if cmd.__name__ == command:
                return cmd(self=self, command=command)
        return "Not a valid command"

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
