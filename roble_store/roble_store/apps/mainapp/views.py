from django.shortcuts import render
from .models import Productos, Categorias
# Create your views here.

def busqueda(request,id):
    if request.method == 'GET':
        identificador=str(id)
        query1="SELECT * FROM testing.mainapp_productos WHERE idCategoria="+identificador
        productos = Productos.objects.raw(query1)
    categorias = Categorias.objects.all()
    contexto = {
        'productos' : productos,
        'categorias' : categorias
    }
      
    return render(request,'index.html', contexto)

def home(request):

    if request.method == 'GET':
        query1="SELECT * FROM testing.mainapp_productos"
        productos = Productos.objects.raw(query1)
    else :
        print('que mierda hace aqui')
        busqueda = request.POST['busqueda']
        query1="SELECT * FROM testing.mainapp_productos WHERE nombreProducto LIKE '%%"+busqueda+"%%'"
        productos = Productos.objects.raw(query1)
    categorias = Categorias.objects.all()
    contexto = {
        'productos' : productos,
        'categorias' : categorias
    }
    return render(request,'index.html', contexto)