from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('login_page/',login_page),
    path('signup_page/',signup_page),
    path('login/',login),
    path('signup/',signup),
]    