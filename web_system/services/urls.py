from django.urls import path
from services.views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from services.views.reporter import ReporterListService

app_name = 'services'

# router = routers.DefaultRouter()
urlpatterns = [
    path('', api_root, name="api-root"),
    path('saudacao', saudacao, name="saudacao"),
    path('calculo',calculo, name="calculo"),
    path('reporter', ReporterListService.as_view(), name='reporter_list'),

]