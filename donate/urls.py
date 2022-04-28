from django.contrib import admin
from django.urls import path, include
# from homepage.views import myView
from . import views

urlpatterns = [

path('donate', views.donate, name='donate'),

]
