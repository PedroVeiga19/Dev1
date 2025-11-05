from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from web_system.views import estaticas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relacionamentos/', include('relacionamentos.urls', namespace="relacionamentos")),
    path('funcao/contato/',views.contato,name='funcao_contato'),
   # path('funcao/search/',views.buscar,name='funcao_buscar'),
    path('', estaticas.index, name="index")
]
