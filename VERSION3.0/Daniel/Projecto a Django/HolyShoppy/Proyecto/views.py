from django.shortcuts import redirect, render
from .models import Producto, Categorias

# Create your views here.

def index(request):
    return render(request,'proyecto/index.html')

def carro(request):
    return render(request,'proyecto/carro.html')

def pagCategorias(request):
    return render(request,'proyecto/Categorias.html')
    
def detallemicro1(request):
    return render(request,'proyecto/detallemicro1.html')

def Electrodomesticos(request):
    listaProductos = Producto.objects.all()
    return render(request,'proyecto/Electrodomesticos.html', {"productos": listaProductos})

def informaciones(request):
    return render(request,'proyecto/informaciones.html')

def promocion(request):
    return render(request,'proyecto/promocion.html')

def registro(request):
    return render(request,'proyecto/registro.html')

def gestionProductos(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categorias.objects.all()
    return render(request, 'proyecto/CRUD/gestionProductos.html', {"productos": listaProductos, "categorias": listaCategorias})

def registrarProducto(request):
    id_producto = request.POST['id_producto']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    nombre_categoria = request.POST['nombreCa']  # Cambio en el nombre del campo
    imagen = request.FILES['imagen']  # Utiliza request.FILES para los archivos
    descripcion = request.POST['descripcion']
    stock = request.POST['stock']

    # Buscar la instancia de Categorias a partir del nombre de categoría seleccionada
    categoria = Categorias.objects.get(nombre_categoria=nombre_categoria)

    # Crear el objeto Producto con la categoría asignada
    producto = Producto.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        precio=precio,
        nombreCa=categoria,  # Asigna la instancia de Categorias
        imagen=imagen,
        descripcion=descripcion,
        stock=stock,
    )
    
    return redirect('gestionProductos')

def editarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    categorias = Categorias.objects.all()  # Obtener todas las categorías disponibles
    return render(request, "proyecto/CRUD/editarProducto.html", {"producto": producto, "categorias": categorias})

def edicionProducto(request):
    id_producto = request.POST['id_producto']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    nombre_categoria = request.POST['nombreCa']  # Cambio en el nombre del campo
    imagen = request.FILES['imagen']  # Utiliza request.FILES para los archivos
    descripcion = request.POST['descripcion']
    stock = request.POST['stock']

    producto = Producto.objects.get(id_producto=id_producto)
    producto.nombre = nombre
    producto.precio = precio
    producto.nombre_categoria = nombre_categoria
    producto.imagen = imagen
    producto.descripcion = descripcion
    producto.stock = stock
    producto.save()

    return redirect('gestionProductos')

def eliminarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()

    return redirect('gestionProductos')
    
