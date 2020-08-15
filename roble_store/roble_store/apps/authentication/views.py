from django.shortcuts import render, redirect
from .models import Clientes

from .forms import ClienteForm

# Create your views here.

def register(request):
    if request.method == 'GET':
        form = ClienteForm
        contexto = {
            'form': form
        }
        return render(request,'login.html', contexto)
    else:
        form = ClienteForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('home')

    