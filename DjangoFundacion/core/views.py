from django.shortcuts import render,redirect
from .models import Obra, Usuario

# Create your views here.
def index(request):
    return render(request, 'core/index.html')