from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('',show_doc_upload_page),
    path('generate/',doc_processing),
    
]    