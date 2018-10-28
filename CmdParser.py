# import courseManager
# import sectionManager
# import userManager
# import authManager

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
    commandList = ['login', 'logout', 'department', 'course', 'section', 'user', 'help', 'exit']
    descriptionList = {'login': "",
                       'logout': "",
                       'department': "",
                       'course': "",
                       'section': "",
                       'user': "",
                       'help': "",
                       'exit': ""}

    # This dictionary contains the a set of key values pairs where the key is the command name and the value is the
    # class the handles all that. It contains department because im still not exactly clear how we're going to deal with
    # the department command without a department manager (or if we even still need a department command). This is
    # useful for formatting the strings to return when testing.
    namesdict = {"user": "PersonManager",
                 "course": "CourseManager",
                 "section": "SectionManager",
                 "department": "DepartmentManger"}

    uting = False  # Unit Testing

    # The only public function of this class that will either call other helper methods to parse any of the larger
    # commands or if the command is simple it parses it itself. Case does not matter for the command, fields won't
    # lose their case.
    @staticmethod
    def parse(command, user='default', testing=uting):
        return ""

    # A helper method to just be used inside this class to parse one of the major commands, course. This also checks
    # auth to insure that the user has perms to do what they're trying to do.
    @staticmethod
    def parseCourse(command, user='default', testing=uting):
        return ""

    # A helper method to just be used inside this class to parse one of the major commands, user. This also checks
    # auth to insure that the user has perms to do what they're trying to do.
    @staticmethod
    def parseUser(command, user='default', testing=uting):
        return ""

    # A helper method to just be used inside this class to parse one of the major commands, section. This also checks
    # auth to insure that the user has perms to do what they're trying to do.
    @staticmethod
    def parseSection(command, user='default', testing=uting):
        return ""

    # A helper method to just be used inside this class to parse one of the major commands, department. This also checks
    # auth to insure that the user has perms to do what they're trying to do.
    @staticmethod
    def parseDept(command, user='default', testing=uting):
        return ""
