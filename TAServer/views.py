# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.views import generic
from django.shortcuts import render, redirect
from django.views import View
from Managers.userManager import UserManager as UM
from Managers.sectionManager import SectionManager as SM
from Managers.courseManager import CourseManager as CM
from Managers.ManagerInterface import ManagerInterface
from TAServer.models import Course
from Managers.DjangoStorageManager import DjangoStorageManager as Storage # Change to whatever we're using now
from TAServer.models import Staff as User
from django.contrib.auth import authenticate, login, logout
from TAServer.forms import SignUpForm


class UserView(View):
    def view(self, request, code=""):
        fields = {}
        template = "user/viewpublic.html" # The default is just to load only public data

        if request.user.is_authenticated and request.user.has_perm('can_view_private'):
            template = "user/viewprivate.html"

        if code != "":
            fields['title'] = "View %s" % code
            fields['data'] = UM(Storage()).view({'username': code})

        else:
            fields['title'] = "View All Users"
            fields['data'] = UM(Storage()).view({})

        fields['datafound'] = len(fields['data']) != 0

        fields['display_edit_link'] = request.user.has_perm("can_edit_user")

        return render(request, template, fields)

    def add(self, request, code=""):
        rolelist = ['TA', 'Instructor', 'Administrator', 'Supervisor']
        fields = {'title': 'Add a new user', 'canedit': False, "role_list": rolelist, 'checked_role': rolelist[0], 'action': '/user/add/'}

        if request.user.has_perm("can_create_user"):
            fields['canedit'] = True

        else:
            fields['value'] = {'username': 'Bad Permissions'}

        return render(request, "user/add.html", fields)

    def edit(self, request, code="", fields={}):
        if code == "":
            return self.add(request)

        rolelist = ['TA', 'Instructor', 'Administrator', 'Supervisor']
        fields['role_list'] = rolelist

        fields['action'] = '/user/edit/%s/' % code

        fields['canedit'] = request.user.has_perm("can_edit_user") or (request.user.username == code and request.user.has_perm("can_edit_self"))

        if fields['canedit']:
            fields['value'] = UM(Storage()).view({'username': code})[0]
            fields['checked_role'] = fields['value']['role']

        else:
            fields['value'] = {'username': 'Bad Permissions'}

        return render(request, "user/add.html", fields)

    def get(self, request, code=""):
        action = request.path.split("/")[2].lower()  # The 'action' of the url (view, add, edit)

        # Just a loop through the different helper functions until the action lines up with a helper function we have.
        for fun in [self.view, self.add, self.edit]:
            if fun.__name__ == action:
                return fun(request, code=code)

        return render(request, "main/index.html") # Should be changed to go to a 404 (django might do this automatically

    def post(self, request, code=""):
        print(request.POST)
        for key in request.POST:
            print("Key: %s\nValue: %s\nTypeof: %s\n" % (key, request.POST[key], type(request.POST[key])))

        rtr = ""

        if "edit" in request.path:
            rtr = UM(Storage()).edit(request.POST)

        elif "add" in request.path:
            rtr = UM(Storage()).add(request.POST)

        else:
            print("Someone sent a post fron %s" % request.path)

        print(rtr)

        status = ""

        if rtr[0]:
            status = "Added Correctly"
        else:
            status = rtr[1]

        return self.edit(request, code=request.POST['username'], fields={'displaystatus': True, 'status': status})  # Just a placeholder

class CourseViews:

    def add(request):
        return render(request, "courses/course_add.html")

    def edit(request, course_id):
        course = CM(Storage()).view({'dept': course_id[:2], 'cnum': course_id[2:]})
        return render(request, "courses/course_edit.html", {'course': course[0]})

    def list(request):
        courses = CM(Storage()).view({})
        return render(request, "courses/course_list.html", {'courses': courses})

    def detail(request, course_id):
        course = CM(Storage()).view({'dept': course_id[:2], 'cnum': course_id[2:]})
        return render(request, "courses/course_detail.html", {'course': course[0]})

class SectionViews:

    def add(request):
        return render(request, "sections/section_add.html")

    def edit(request, section_id):
        section = SM(Storage()).view({'cnum': section_id[:3], 'snum': section_id[3:]})
        return render(request, "sections/section_edit.html", {'section': section[0]})

    def list(request):
        sections = SM(Storage()).view({})
        return render(request, "sections/section_list.html", {'sections': sections})

    def detail(request, section_id):
        section = SM(Storage()).view({'cnum': section_id[:3], 'snum': section_id[3:]})
        return render(request, "sections/section_detail.html", {'section': section[0]})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def About(request):
    return render(request, "main/about.html")

def FAQ(request):
    return render(request, "main/FAQ.html")

def error_404(request):
    data = {}
    return render(request, '404.html', data)

def error_500(request):
    data = {}
    return render(request, '500.html', data)

class Home(View):
    def get(self, request):
        return render(request, "main/index.html")
