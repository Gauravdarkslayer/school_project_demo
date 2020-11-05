from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('choose/',choose),
    path('login_page/',login_page),
    path('signup/',signup),
    path('login/',login),
    path('signup_page/',signup_page),
    path('',homepage),

]    