from django.contrib import admin
from django.urls import path, include
# from homepage.views import myView
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('home', views.home, name="homepage"),
path('signup', views.signup, name='signup'),
path('signin', views.signin, name='signin'),
path('signout', views.signout, name='signout'),
path('signin_user', views.signin_user, name="signin_user"),
]
