# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.shortcuts import render
from django.views import View
from Managers.userManager import UserManager as UM
from Managers.sectionManager import SectionManager as SM
from Managers.courseManager import CourseManager as CM
from Managers.ManagerInterface import ManagerInterface
from Managers.DjangoStorageManager import DjangoStorageManager as Storage # Change to whatever we're using now
from TAServer.models import Staff as User
from TAServer.models import DefaultGroup, TAGroup, InsGroup, AdminGroup, SupGroup
from django.contrib.auth import authenticate, login, logout


# This is a very fast and loose way to validate everything. I'm basically assuming that if you've got ins or ta in your
# command you're trying to assign them to something because user view uses other field names. If a user is not provided
# construct the default one (assuming that the default one will have the default permissions level)
# Bugs: Doesn't check what the user is trying to edit
def validate(cmd: dict, usr: User = None)->bool:
    return True
    # if 'ta' in cmd:
    #     return usr.has_perm("can_assign_ta")
    #
    # if 'ins' in cmd:
    #     return usr.has_perm("can_assign_ins")
    #
    # return usr.has_perm("can_%s_%s" % (cmd['action'], cmd['command'])) # This catches most cases

    permDict = {'T': TAGroup, 'I': InsGroup, 'A': AdminGroup, 'S': SupGroup}

    permGroup = DefaultGroup
    checkPerm = ""

    if usr is not None:
        permGroup = permDict[usr.role]

    if 'ta' in cmd:
        checkPerm = "can_assign_ta"

    elif 'ins' in cmd:
        checkPerm = "can_assign_ins"

    else:
        checkPerm = "can_%s_%s" % (cmd['action'], cmd['command'])

    print("checking %s is in %s" % (checkPerm, permGroup.__name__))

    for perm in permGroup.permissions:
        if perm[0] == checkPerm:
            return True

    return False

# The general manager command parser. The manager has already been picked by another function an as long as it
# implements the interface, this will all work. It checks that all the required fields are there, makes any missing
# optional fields none, and removes any fields not in the optional or required fields. After this it makes sure the user
# has the correct permissions before calling the correct function and returning it's value (or the state of the return
# if the function returns a boolean).
def mgr(mgr: ManagerInterface, command: str, request) -> str:
    cmddict = fieldsToDict(command)

    if request.user.is_authenticated:
        print("User is authenticated")
        if not validate(cmddict, request.user):
            return "Bad Permissions"
    elif not validate(cmddict):
        return "Bad Permissions"

    for field in mgr.reqFields(): # Make sure all required fields are there
        if field not in cmddict and cmddict['action'] != 'view':
            return "Missing field: %s" % field

    for field in mgr.optFields(): # Make sure all optfields are set to None if they're not in there
        if field not in cmddict:
            cmddict[field] = None

    for field in cmddict.copy(): # Remove all fields not in the manager. A copy because you cant remove from a dict while iterating through it
        if field not in mgr.optFields() and field not in mgr.reqFields() and field is not 'action' and field is not 'command':
            del cmddict[field]

    print(cmddict)

    if(cmddict['action'] == 'view'):
        return mgr.view(cmddict)

    for func in [mgr.add, mgr.delete, mgr.edit]:
        if(cmddict['action'] == func.__name__):
            if(func(cmddict)):
                return "Success"
            return "Failure"

    return "No dice"


# Calls the general manager command with the course manager correctly initialized
def course(command: str, request) -> str:
    return mgr(CM(Storage()), command, request)


# Calls the general manager command with the section manager correctly initialized
def section(command: str, request) -> str:
    return mgr(SM(Storage()), command, request)


# Calls the general manager command with the user manager correctly initialized
def user(command: str, request) -> str:
    return mgr(UM(Storage()), command, request)


# Sets the user for the request with the authenticate and login command. Returning success or failure depending on if
# the user is able to log in
def checkLogin(command: str, request) -> str:
    split = command.split(" ")
    if(len(split) < 3):
        return "Invalid use"

    u = authenticate(request, username=split[1], password=split[2])

    if(u is not None):
        login(request, user)
        return "Success"
    return "Failure"


# Logs the user out (django's logout function just clears session data so idk really how do even tell if a user was
# logged in in the first place so it always retusn Success
def checkLogout(command: str, request) -> str:
    if(not request.user.is_authenticated):
        return "Failure"
    logout(request) # All this does is clear session data for the request which happens to include the user
    return "Success"


descriptionList = {'login': "Placeholder description for login",
                   'logout': "Placeholder description for logout",
                   'course': "Placeholder description for course",
                   'section': "Placeholder description for section",
                   'user': "Placeholder description for user",
                   'help': "Placeholder description for help"}

# Parses the help command
def help(command: str, request) -> str:
    split = command.lower().split(' ')

    if(len(split) == 1):
        return "This is the default help command response"

    if(split[1] not in descriptionList):
        return "%s is not a valid command" % split[1]
    return descriptionList[split[1]]


# This needs to be here to see all the above functions as handles
commandList = [checkLogin, checkLogout, course, section, user, help]


# Finds the right function to call and calls it
# This is currently just a proof of concept to show how we could implement the way rock did it in the lab without
# having to call ever command and check what they return and ahve to check in each command function if they're the
# right one.
def parse(request) -> str:
    command = request.POST["command"].split(' ')[0].lower()

    for cmd in commandList:
        if cmd.__name__.lower() == command:
            return cmd(request.POST["command"], request)
    return "Not a valid command"


# Returns None when a something is invalid in the command
def fieldsToDict(cmd: str) -> dict:
    rtr = {}
    split = cmd.split(" ") # If someone is a regex wiz lmk
    if(len(split) < 2):
        return {}

    rtr['command'] = split.pop(0).lower()
    rtr['action'] = split.pop(0).lower()

    lastField = ""
    while(len(split) > 0): # While there is more data in the list
        pop = split.pop(0) # Get the first element of the array and remove it

        if("=" in pop): # If what was removed had a = in in EX: role=TA
            fieldSplit = pop.split("=")

            if(len(fieldSplit) < 2):
                return {}

            lastField = fieldSplit[0]

            rtr[fieldSplit[0]] = fieldSplit[1]

        else: # This means that it is not a field and needs to be added back to a field
            if(lastField == ""):
                return {}

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
        return render(request, "main/index.html", {"out": parse(request)})