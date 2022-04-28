from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

path('hospital_signin', views.hospital_signin, name='hospital_signin'),
path('hospital_signout', views.hospital_signout, name='hospital_signout'),
path('hospital_account', views.hospital_account, name='hospital_account'),

]
