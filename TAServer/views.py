# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.shortcuts import render
from django.views import View

def addUser(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

def addItem(args):
  #if args[0] == "addItem", adds item args[1] to user args[2]
  #returns "Item <args[1]> added to user <args[2]>"
  #or "User <args[2]> already has item <args[1]>"
  #or "User <args[2]> does not exist"
  #else returns ""
  if args[0] == "addItem":
    return "I am addItem"
  else:
     return ""

def display(args):
  #if args[0] == display
  #return a string with each user followed by their items
  #items are indented
  if args[0] == "display":
    return "I am display"
  else:
     return ""

commandList = [addUser, addItem, display]
def doStuff(s, commandList):
  args = s.split(" ")
  for i in commandList:
    out = i(args)
    if out != "": #if i matches arg[0], stop looping
      break
  if out == "":
    out = "command not found"
  return out

# Create your views here.

class Home(View):
  def get(self,request):
    return render(request,"main/index.html")
  def post(self,request):
    out = doStuff(request.POST["command"],commandList)
    return render(request,"main/index.html", {"out":out})
