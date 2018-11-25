# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.shortcuts import render
from django.views import View
from Managers.userManager import UserManager as UM
from Managers.sectionManager import mySectionManager as SM
from Managers.courseManager import CourseManager as CM
from Managers.authManager import AuthManager as AM
from Managers.ManagerInterface import ManagerInterface
from Managers.JSONStorageManager import JSONStorageManager as Storage # Change to whatever we're using now

class User: # Just so python doesn't get mad
    pass


def mgr(mgr: ManagerInterface, command: str) -> str:
    cmddict = fieldsToDict(command)

    for field in mgr.reqFields(): # Make sure all required fields are there
        if field not in cmddict:
            return "Invalid command"

    for field in mgr.optFields(): # Make sure all optfields are set to None if they're not in there
        if field not in cmddict:
            cmddict[field] = None

    for field in cmddict: # Remove all fields not in the manager
        if field not in mgr.optFields() and field not in mgr.reqFields():
            del cmddict[field]

    if(cmddict['action'] == 'view'):
        return mgr.view(cmddict)

    for func in [mgr.add, mgr.delete, mgr.edit]:
        if(cmddict['action'] == func.__name__):
            if(func(cmddict)):
                return "Success"
            return "Failure"


# Parses the course command
def course(command: str) -> str:
    mgr(CM(Storage()), command)


# Parses the section command
def section(command: str) -> str:
    mgr(SM(Storage()), command)


# Parses the user command
def user(command: str) -> str:
    mgr(UM(Storage()), command)


# Parses the login command
def login(command: str) -> str:
    pass


# Parses the logout command
def logout(command: str) -> str:
    pass


descriptionList = {'login': "Placeholder description for login",
                   'logout': "Placeholder description for logout",
                   'course': "Placeholder description for course",
                   'section': "Placeholder description for section",
                   'user': "Placeholder description for user",
                   'help': "Placeholder description for help",
                   'exit': "Placeholder description for exit"}

# Parses the help command
def help(command: str) -> str:
    want = command.split(' ')[1].lower() # What the user wants help with. Splits the command into splaces, gets the first one, and gets the lower case of that

    if(want not in descriptionList):
        return "Not a valid command"
    return descriptionList[want]


# Parses the exit command
def exit(command: str) -> str: # Deprecated?
    pass


# This needs to be here to see all the above functions as handles
commandList = [login, logout, course, section, user, help, exit]


# Finds the right function to call and calls it
# This is currently just a proof of concept to show how we could implement the way rock did it in the lab without
# having to call ever command and check what they return and ahve to check in each command function if they're the
# right one.
def parse(post: str, user: User = None) -> str:
    command = post.split(' ')[0].lower()

    for cmd in commandList:
        if cmd.__name__ == command:
            return cmd(command)
    return "Not a valid command"


# Returns None when a something is invalid in the command
def fieldsToDict(cmd: str) -> dict:
    rtr = {}
    split = cmd.split(" ") # If someone is a regex wiz lmk
    if(len(split) < 2):
        return None

    rtr['command'] = split.pop(0).lower()
    rtr['action'] = split.pop(0).lower()

    lastField = ""
    while(len(split) > 0): # While there is more data in the list
        pop = split.pop(0) # Get the first element of the array and remove it

        if("=" in pop): # If what was removed had a = in in EX: role=TA
            fieldSplit = pop.split("=")

            if(len(fieldSplit) < 2):
                return None

            lastField = fieldSplit[0]

            rtr[fieldSplit[0]] = fieldSplit[1]

        else: # This means that it is not a field and needs to be added back to a field
            if(lastField == ""):
                return None

            rtr[lastField] += " "+pop

        if 'code' in rtr: # If the dict has a key called code (which needs to be parsed itself)
            codedict = codeToDict(rtr['code'])
            del rtr['code'] # Remove the code entry from our dict (weird syntax ik)

            for k in codedict: # For each key in the code dict add it to our dict
                rtr[k] = codedict[k]

    return rtr


# Hopefully the last helper method, used to convert a code to a dictionary of it's parts
# EX: "code=CS-351-601" -> {'dept': 'CS', 'cnum': '351', 'snum': '601'}
def codeToDict(code: str) -> dict:
    cArr = code.split("-")
    rtr = {'dept': cArr[0]}  # the [5:] removes the code= part

    if (len(cArr) > 1):
        rtr['cnum'] = cArr[1]

    if (len(cArr) > 2):
        rtr['snum'] = cArr[2]

    return rtr

class Home(View):
    def get(self, request):
        return render(request, "main/index.html")

    def post(self, request):
        out = parse(request.POST["command"])
        return render(request, "main/index.html", {"out": out})
