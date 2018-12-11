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
from TAServer.models import DefaultGroup, TAGroup, InsGroup, AdminGroup, SupGroup
from django.contrib.auth import authenticate, login, logout
from TAServer.forms import SignUpForm


from django.db.utils import OperationalError


class CourseListView(generic.ListView):
    try:
        model = Course
        context_object_name = 'courses'
        queryset = CM(Storage()).view({})
        template_name = 'courses/course_list.html'
    except OperationalError:
        pass  # db doesnt exist yet
    

def courseDetail(request, course_id):
    course = CM(Storage()).view({'dept': course_id[:2], 'cnum': course_id[2:]})
    context = {'course': course[0]}
    return render(request, "courses/course_detail.html", context)

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
