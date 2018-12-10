# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_view
from TAServer import views
from TAServer.views import Home
from django.conf.urls import handler404

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', Home.as_view()),
  url('^home/', Home.as_view(), name='home'),
  url(r'^login/$', auth_view.LoginView.as_view(), {'template_name': '/registration/login.html'}, name='login'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^FAQ/', views.FAQ, name='faq'),
]

handler404 = views.error_404
handler500 = views.error_500