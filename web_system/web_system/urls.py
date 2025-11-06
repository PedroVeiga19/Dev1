from tkinter.font import names

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from web_system.views.estaticas import index
from web_system.views.contato import contact
from .views.contato_classe import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relacionamentos/', include('relacionamentos.urls', namespace="relacionamentos")),
    path('classe/contato/',ContactView.as_view(),name="classe_contato"),
    path('funcao/contato/',contact,name='funcao_contato'),
   # path('funcao/search/',views.buscar,name='funcao_buscar'),
    path('', index, name="index")
]
