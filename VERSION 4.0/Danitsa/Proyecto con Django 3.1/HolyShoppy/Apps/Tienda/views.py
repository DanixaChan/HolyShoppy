from django.shortcuts import redirect,get_object_or_404,render,HttpResponseRedirect
from .models import Usuario,Pago,Detalleproducto,Producto,Categorias
from django.contrib import messages
from .forms import UsuarioForm,LoginForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def carro(request):
    return render(request,'productos/carro.html')

def pagCategorias(request):
    return render(request,'productos/Categorias.html')
    
def detallemicro1(request):
    return render(request,'productos/detallemicro1.html')

def Electrodomesticos(request):
    listaProductos = Producto.objects.all()
    return render(request,'productos/Electrodomesticos.html', {"productos": listaProductos})

def informaciones(request):
    return render(request,'productos/informaciones.html')

def promocion(request):
    return render(request,'productos/promocion.html')

def gestionProductos(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categorias.objects.all()
    return render(request, 'productos/CRUD/gestionProductos.html', {"productos": listaProductos, "categorias": listaCategorias})

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
        nombre_categoria=categoria,  # Asigna la instancia de Categorias
        imagen=imagen,
        descripcion=descripcion,
        stock=stock,
    )
    
    return redirect('gestionProductos')

def editarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    categorias = Categorias.objects.all()  # Obtener todas las categorías disponibles
    return render(request, "productos/CRUD/editarProducto.html", {"producto": producto, "categorias": categorias})

# def edicionProducto(request):
#     id_producto = request.POST['id_producto']
#     nombre = request.POST['nombre']
#     precio = request.POST['precio']
#     nombre_categoria = request.POST['nombreCa']  # Cambio en el nombre del campo
#     imagen = request.FILES['imagen']  # Utiliza request.FILES para los archivos
#     descripcion = request.POST['descripcion']
#     stock = request.POST['stock']

#     producto = Producto.objects.get(id_producto=id_producto)
#     producto.nombre = nombre
#     producto.precio = precio
#     producto.nombre_categoria = nombre_categoria
#     producto.imagen = imagen
#     producto.descripcion = descripcion
#     producto.stock = stock
#     producto.save()

#     return redirect('gestionProductos')

def edicionProducto(request):
    id_producto = request.POST['id_producto']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    nombre_categoria = request.POST['nombreCa']
    imagen = request.FILES['imagen']
    descripcion = request.POST['descripcion']
    stock = request.POST['stock']

    producto = get_object_or_404(Producto, id_producto=id_producto)
    categoria = get_object_or_404(Categorias, nombre_categoria=nombre_categoria)

    producto.nombre = nombre
    producto.precio = precio
    producto.nombre_categoria = categoria
    producto.imagen = imagen
    producto.descripcion = descripcion
    producto.stock = stock
    producto.save()

    return redirect('gestionProductos')

def eliminarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()

    return redirect('gestionProductos')
    




def logout(request):
     logout(request)
     messages.success(request,'You have been logged out.')
     return redirect('home')

def home(request): 
    return render(request, 'home.html')

def registro(request):
    return render(request, 'usuarios/registro.html')

def editUser(request): 
    return render(request, 'usuarios/editUser.html')

def listUser(request): 
    usuarios=Usuario.objects.all()
    return render(request, 'usuarios/listUser.html', {'usuarios': usuarios})

def PagosList():
    pagos=Pago.objects.all()
    return pagos

def UsuarioAdd(request):
    context = {'form': UsuarioForm(), 'pagos': PagosList()}
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context = {'mensaje': "Usuario registrado con éxito!"}
        else:
            return render(request, 'usuarios/registro.html', {'form': formulario})
    return render(request, 'usuarios/registro.html', context)

def UsuarioDelete(request, form_user):
    usuario=Usuario.objects.get(form_user=form_user)
    usuario.delete()
    return redirect('/listUser')

def edicionUsuario(request, form_user):
    usuario = Usuario.objects.get(form_user=form_user)
    return render(request, "usuarios/edicionUsuario.html", {"usuario": usuario, 'pagos': PagosList()})


def UsuarioEdit(request, form_user):
    usuario = get_object_or_404(Usuario, form_user=form_user)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            payment_card_name = request.POST.get('form_payment_card')
            payment_card = get_object_or_404(Pago, form_payment_card=payment_card_name)
            usuario.form_payment_card = payment_card
            form.save()
            return redirect('/listUser')
        else:
            print(form.errors)

    return redirect('/listUser')

@login_required
def login_view(request):
    return redirect('home')