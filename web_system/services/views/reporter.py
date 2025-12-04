from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from relacionamentos.models.reporter import Reporter
from services.serializers.reporter import ReporterMinimaSerlializer
#from services.views import BaseSecurity

class ReporterListService(APIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterMinimaSerlializer

    def get(self, request, format=None):
        exemplos = Reporter.objects.all()
        context = {
            'request': request,
            'format': format
        }
        serializer = ReporterMinimaSerlializer(exemplos, many=True, context=context)

        return Response(serializer.data)
    
    def post(self, request, format=None):
        dados = request.data
        context = {
            'request': request,
            'format': format,
        }
        serializer = ReporterMinimaSerlializer(data=dados, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, statu=status.HTTP_400_BAD_REQUEST)