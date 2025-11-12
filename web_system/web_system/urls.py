from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from web_system.views.estaticas import index
from web_system.views.contato import contact
from .views.contato_classe import ContactView
from django.contrib.auth import views as auth_views
from .forms.custom_login_form import CustomLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relacionamentos/', include('relacionamentos.urls', namespace="relacionamentos")),
    path('classe/contato/',ContactView.as_view(),name="classe_contato"),
    path('funcao/contato/',contact,name='funcao_contato'),
   # path('funcao/search/',views.buscar,name='funcao_buscar'),
    path('', index, name="index"),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html",
                                      authentication_form=CustomLoginForm), name="login"),
    path('accounts/', include('django.contrib.auth.urls')),

]
