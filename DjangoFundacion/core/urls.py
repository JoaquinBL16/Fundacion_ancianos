from django.urls import path, include
from .views import index,login,register,inicio_donador
from django.conf import settings


urlpatterns = [
    path('', index, name="index"),

    #carpeta de acceso
    path('acceso/login/', login, name="login"),
    path('acceso/register/', register, name="register"),

    #carpeta de donador 
    path('donador/inicio/',inicio_donador, name="inicio_donador" ),
]
