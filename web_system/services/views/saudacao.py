from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse 
from rest_framework.views import APIView 


@api_view(['GET'])
def saudacao(request):
    return Response({'saudacao':'Ola Mundo'})



@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'saudacao' : reverse('services:saudacao',request=request,format=format)
    })