from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from web_system import views
from django.contrib.auth import views as auth_views
from web_system.forms import CustomLoginForm
from web_system.views.profile import ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('relacionamentos/', include('relacionamentos.urls', namespace="relacionamentos")),
    path('services/',include('services.urls',namespace="services")),
    path('', views.estaticas.index, name="index"),
    path('funcao/contato/', views.contact, name="function_contact"),
    #path('funcao/search/', views.buscar, name="search_function"),
    path('class/contato/', views.ContactView.as_view(), name="class_contact"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="accounts/login.html", authentication_form=CustomLoginForm)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]