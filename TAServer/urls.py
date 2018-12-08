# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_view
from TAServer import views
from TAServer.views import Home

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url('^home/', Home.as_view()),
  url(r'^login/$', auth_view.LoginView.as_view(), {'template_name': '/registration/login.html'}),
  url(r'^signup/$', views.signup, name='signup'),

]
