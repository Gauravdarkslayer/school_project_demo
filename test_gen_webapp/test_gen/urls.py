from django.conf.urls import include
from django.urls import path
from .views import *

app_name = 'test_gen'

urlpatterns = [
    path('',show_doc_upload_page,name='upload_question'),
    path('register_org/',register_new_org,name='register_new_org'),
    path('preview_test/',preview),
    path('generate/',doc_processing),
    
]    