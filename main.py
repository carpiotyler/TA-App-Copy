from CmdParser import CommandParser as parser

p = parser()

while(True):
    if(p.currentUser() is None):
        print(p.parse(input("None:$ ")), '\n')

    else:
        print(p.parse(input("%s:$ " % p.currentUser().username)), '\n')