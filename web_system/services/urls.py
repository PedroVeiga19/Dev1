from django.urls import path 
from services.views import *


app_name = 'services'


urlpatterns = [
    path('',api_root,name="api-root"),
    path('saudacao',saudacao,name="saudacao"),
]