from django.contrib import admin
from django.urls import path, include
# from homepage.views import myView
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('home', views.home, name="homepage"),
path('user_signup', views.user_signup, name='user_signup'),
path('user_signin', views.user_signin, name='user_signin'),
path('user_signout', views.user_signout, name='user_signout'),
path('user_account', views.user_account, name="user_account"),
path('change_password_page', views.change_password_page, name="change_password_page"),
path('change_password', views.change_password, name="change_password"),
]
