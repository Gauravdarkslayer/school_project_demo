from django.conf.urls import include
from django.urls import path
from .views import *

app_name = 'test_gen'

urlpatterns = [
    path('',show_doc_upload_page,name='upload_question'),
    path('generate/',doc_processing),
    
]    