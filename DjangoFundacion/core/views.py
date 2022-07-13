from django.shortcuts import render,redirect
from .models import Usuario

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def login(request):
    if request.method=='POST':
        currentEmail = request.POST.get('userEmail')
        currentPassword = request.POST.get('userPassword')
        if currentEmail == 'admin@gmail.com' and currentPassword == 'admin':
            return render(request, 'core/administrador/inicio/index.html')
        for dbEmail in Usuario.objects.values_list('email', flat=True):
            if currentEmail == dbEmail:
                dbPassword = Usuario.objects.values_list('contraseña', flat=True).get(email=dbEmail)
                if currentPassword == dbPassword:
                    return render(request, 'core/usuario/inicio/index.html')
            
    # dbEmail = Usuario.objects.values_list('email', flat=True).get(email=currentEmail)
    # if dbEmail:
    #     return render(request, 'core/usuario/inicio/index.html')
    #     dbPassword = Usuario.objects.values_list('contraseña').filter(email=currentEmail)
    #     if currentPassword == '123456':
    #         return render(request, 'core/usuario/inicio/index.html')
    return render(request, 'core/acceso/login/index.html')
            
def register(request):
    contexto = {}
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('email') and request.POST.get('contraseña'):
            usuario=Usuario()
            usuario.nombre= request.POST.get('nombre')
            usuario.apellido= request.POST.get('apellido')
            usuario.email= request.POST.get('email')
            usuario.contraseña= request.POST.get('contraseña')
            usuario.save()
            contexto['mensaje']='Usuario registrado correctamente!'

    return render(request, 'core/acceso/register/index.html', contexto)

def inicio_donador(request):
    return render (request,'core/donador/inicio/index.html')
