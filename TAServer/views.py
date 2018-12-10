# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.shortcuts import render, redirect
from django.views import View
from Managers.userManager import UserManager as UM
from Managers.sectionManager import SectionManager as SM
from Managers.courseManager import CourseManager as CM
from Managers.ManagerInterface import ManagerInterface
from Managers.DjangoStorageManager import DjangoStorageManager as Storage # Change to whatever we're using now
from TAServer.models import Staff as User
from TAServer.models import DefaultGroup, TAGroup, InsGroup, AdminGroup, SupGroup
from django.contrib.auth import authenticate, login, logout
from TAServer.forms import SignUpForm


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


class UserView(View):
    def view(self, request, code=""):
        mgr = UM(Storage()) # Hopefully this is correct
        fields = {}
        template = "user/viewpublic.html"

        if request.user.is_authenticated and request.user.has_perm('can_view_private'):  # Redundant?
            template = "user/viewprivate.html"

        if code != "":
            fields['title'] = "View all users"
            fields['data'] = mgr.view({'username': code})

        else:
            fields['title'] = "View %s" % code
            fields['data'] = mgr.view({})  # Hopefully this is correct

        fields['datafound'] = len(fields['data']) == 0

        return render(request, template, fields)

    def add(self, request, code=""):
        return render(request, "user/add.html", {'title': code})

    def edit(self, request, code=""):
        return render(request, "user/add.html", {'title': code})

    def get(self, request, code=""):
        action = request.path.split("/")[2].lower()  # The 'action' of the url (view, add, edit)

        # Just a loop through the different helper functions until the action lines up with a helper function we have.
        for fun in [self.view, self.add, self.edit]:
            if fun.__name__ == action:
                return fun(request, code=code)

        return render(request, "main/index.html") # Should be changed to go to a 404 (django might do this automatically

    def post(self, request, code=""):
        return self.get(request, code=code)  # Just a placeholder


class Home(View):
    def get(self, request):
        return render(request, "main/index.html")
