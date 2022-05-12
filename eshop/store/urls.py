from .views import index, signup
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',index , name='homepage'),
    path('signup',signup)
]
