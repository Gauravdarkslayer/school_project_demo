from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('choose/',choose),
    path('signup/',signup),
    path('login/',login),
    path('signup_page/',signup_page),
    path('',homepage),

]    