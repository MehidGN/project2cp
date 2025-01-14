from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from . import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]