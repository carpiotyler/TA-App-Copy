# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_view
from TAServer import views
from TAServer.views import Home
from django.conf.urls import handler404

urlpatterns = [
  url(r'^$', Home.as_view()),
  url(r'^home/', Home.as_view(), name='home'),
  url(r'^admin/', admin.site.urls),
  url(r'^login/$', auth_view.LoginView.as_view(), {'template_name': '/registration/login.html'}, name='login'),
  url(r'^logout/$', auth_view.LogoutView.as_view(), name='logout'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^courses/$', views.courseList, name='Course List'),
  url(r'^courses/(?P<course_id>\w+)/$', views.courseDetail, name='course'),
  url(r'^sections/$', views.sectionList, name='Section List'),
  url(r'^sections/(?P<section_id>\w+)/$', views.sectionDetail, name='section'),
  url(r'^FAQ/', views.FAQ, name='faq'),
  url(r'^about/', views.About, name='about'),
  path('user/add/', views.UserView.as_view(), name='User Add'),  # Add a new one
  path('user/edit/<str:code>/', views.UserView.as_view(), name='User Edit'),  # Edit a specific one
  path('user/view/', views.UserView.as_view(), name='User List'),  # View all
  path('user/view/<str:code>/', views.UserView.as_view(), name='User Detail'),  # View one
]


handler404 = views.error_404
handler500 = views.error_500
