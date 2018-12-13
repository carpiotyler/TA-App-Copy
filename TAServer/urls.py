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

  url(r'^FAQ/', views.FAQ, name='faq'),
  url(r'^about/', views.About, name='about'),
  url(r'^courses/$', views.CourseViews.list, name='Course List'),
  url(r'^courses/add', views.CourseViews.add, name='Course Add'),
  url(r'^courses/(?P<course_id>\w+)/$', views.CourseViews.detail, name='Course Detail'),
  url(r'^courses/edit/(?P<course_id>\w+)/$', views.CourseViews.edit, name='Course Edit'),

  url(r'^sections/$', views.SectionViews.list, name='Section List'),
  url(r'^sections/add', views.SectionViews.add, name='Section Add'),
  url(r'^sections/(?P<section_id>\w+)/$', views.SectionViews.detail, name='Section Detail'),
  url(r'^sections/edit/(?P<section_id>\w+)/$', views.SectionViews.edit, name='Section Edit'),

  path('user/add/', views.UserView.as_view(), name='User Add'),  # Add a new one
  path('user/edit/<str:code>/', views.UserView.as_view(), name='User Edit'),  # Edit a specific one
  path('user/view/', views.UserView.as_view(), name='User List'),  # View all
  path('user/view/<str:code>/', views.UserView.as_view(), name='User Detail'),  # View one
]


handler404 = views.error_404
handler500 = views.error_500
