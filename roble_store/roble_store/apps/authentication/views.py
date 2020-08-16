from django.shortcuts import render, redirect
from .models import Clientes
from roble_store.apps.mainapp.views import home
from .forms import ClienteForm

# Create your views here.

def register(request):
    print('entrando por get')
    if request.method == 'GET':
        form = ClienteForm
        contexto = {
            'form': form
            
        }
        
        return render(request,'login.html', contexto)
        
    if request.method == 'POST':
        print('entrando por post')
        form = ClienteForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            print('formulario valido')
            form.save()
            return redirect('home')
        else: print('formulario no es valido')