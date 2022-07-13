from django.urls import path, include
from .views import index,login,register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('acceso/login/', login, name="login"),
    path('acceso/register/', register, name="register"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )