from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_view
from TAServer import views
from TAServer.views import Home

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', Home.as_view()),
    url('^home/', Home.as_view()),

    url(r'^login/$', auth_view.LoginView.as_view(), {'template_name': '/registration/login.html'}, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

    # Added for viewing users
    path('user/add/', views.UserView.as_view()),              # Add a new one
    path('user/edit/<str:code>/', views.UserView.as_view()),  # Edit a specific one
    path('user/view/', views.UserView.as_view()),             # View all
    path('user/view/<str:code>/', views.UserView.as_view()),  # View one

]
