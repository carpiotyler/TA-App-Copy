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



def courseList(request):
    courses = CM(Storage()).view({})
    return render(request, "courses/course_list.html", {'courses': courses})

def courseDetail(request, course_id):
    course = CM(Storage()).view({'dept': course_id[:2], 'cnum': course_id[2:]})
    return render(request, "courses/course_detail.html", {'course': course[0]})

def sectionList(request):
    sections = SM(Storage()).view({})
    return render(request, "sections/section_list.html", {'sections': sections})

def sectionDetail(request, section_id):
    section = SM(Storage()).view({'cnum': section_id[:3], 'snum': section_id[3:] })
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
