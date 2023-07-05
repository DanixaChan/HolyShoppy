from django.http import HttpResponseForbidden
from django.shortcuts import redirect,get_object_or_404,render,HttpResponseRedirect
from .models import Usuario,Pago,Detalleproducto,Producto,Categorias
from django.contrib import messages
from .forms import UsuarioForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Acceso denegado")  # Otra respuesta adecuada para usuarios no autorizados
    return wrapper

def carro(request):
    return render(request,'productos/carro.html')

def pagCategorias(request):
    return render(request,'productos/Categorias.html')
    
def detallemicro1(request):
    return render(request,'productos/detallemicro1.html')

def Electrodomesticos(request):
    categoria = Categorias.objects.get(nombre_categoria='Electrodomesticos')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/Electrodomesticos.html', {"productos": listaProductos})

def tecnologia(request):
    categoria = Categorias.objects.get(nombre_categoria='tecnologia')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/tecnologia.html', {"productos": listaProductos})

def servicioTecnico(request):
    categoria = Categorias.objects.get(nombre_categoria='servicioTecnico')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/servicioTecnico.html', {"productos": listaProductos})

def materialesDIY(request):
    categoria = Categorias.objects.get(nombre_categoria='materialesDIY')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/materialesDIY.html', {"productos": listaProductos})

def gasfiteria(request):
    categoria = Categorias.objects.get(nombre_categoria='gasfiteria')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/gasfiteria.html', {"productos": listaProductos})

def herramientas(request):
    categoria = Categorias.objects.get(nombre_categoria='herramientas')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/herramientas.html', {"productos": listaProductos})

def calzado(request):
    categoria = Categorias.objects.get(nombre_categoria='calzado')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/calzado.html', {"productos": listaProductos})

def belleza(request):
    categoria = Categorias.objects.get(nombre_categoria='belleza')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/belleza.html', {"productos": listaProductos})

def aseo(request):
    categoria = Categorias.objects.get(nombre_categoria='aseo')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/aseo.html', {"productos": listaProductos})

def arriendo(request):
    categoria = Categorias.objects.get(nombre_categoria='arriendo')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/arriendo.html', {"productos": listaProductos})

def utilesEscolares(request):
    categoria = Categorias.objects.get(nombre_categoria='utilesEscolares')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/utilesEscolares.html', {"productos": listaProductos})

def empleo(request):
    categoria = Categorias.objects.get(nombre_categoria='empleo')
    listaProductos = Producto.objects.filter(nombre_categoria=categoria)
    return render(request, 'productos/empleo.html', {"productos": listaProductos})

def informaciones(request):
    return render(request,'productos/informaciones.html')

def promocion(request):
    return render(request,'productos/promocion.html')

def registro(request):
    return render(request,'usuarios/registro.html')

@login_required
@admin_required
def gestionProductos(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categorias.objects.all()
    return render(request, 'productos/CRUD/gestionProductos.html', {"productos": listaProductos, "categorias": listaCategorias})

def registrarProducto(request):
    id_producto = request.POST['id_producto']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    nombreCa = request.POST['nombreCa']  # Actualizar el nombre del campo
    imagen = request.FILES['imagen']  # Utiliza request.FILES para los archivos
    descripcion = request.POST['descripcion']
    stock = request.POST['stock']

    # Buscar la instancia de Categorias a partir del nombre de categoría seleccionada
    categoria = Categorias.objects.get(nombre_categoria=nombreCa)

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
    producto.categoria = nombre_categoria
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
    pagos=Pago.objects.all()
    context = {'form': UsuarioForm(), 'pagos': pagos}
    return render(request, 'usuarios/registro.html', context)

def editUser(request): 
    return render(request, 'usuarios/editUser.html')

@login_required
@admin_required
def listUser(request): 
    usuarios=Usuario.objects.all()
    return render(request, 'usuarios/listUser.html', {'usuarios': usuarios})

def UsuarioAdd(request):
    pagos=Pago.objects.all()
    context = {'form': UsuarioForm(), 'pagos': pagos}
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context = {'form': UsuarioForm(), 'pagos': pagos, 'mensaje': "Usuario registrado con éxito!"}
            messages.success(request, 'Usuario registrado con éxito!')
            return render(request, 'usuarios/registro.html', context)  # Redirige a la página de registro exitoso
        else:
            print(formulario.errors)
            messages.error(request, 'Ha ocurrido un error al registrar el usuario. Por favor, verifica los datos.')
    else:
        formulario = UsuarioForm()
    return render(request, 'usuarios/registro.html', context)

def UsuarioDelete(request, form_user):
    usuario=Usuario.objects.get(form_user=form_user)
    user = User.objects.get(username=usuario.form_user)
    usuario.delete()
    user.delete()
    return redirect('/listUser')

def edicionUsuario(request, form_user):
    pagos=Pago.objects.all()
    usuario = Usuario.objects.get(form_user=form_user)
    return render(request, "usuarios/edicionUsuario.html", {"usuario": usuario, 'pagos': pagos})


def UsuarioEdit(request, form_user):
    usuario = get_object_or_404(Usuario, form_user=form_user)
    user = get_object_or_404(User, username=usuario.form_user)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            payment_card_name = request.POST.get('form_payment_card')
            payment_card = get_object_or_404(Pago, form_payment_card=payment_card_name)
            usuario.form_payment_card = payment_card
            form.save()
            user.email = usuario.form_correo
            user.first_name = form.cleaned_data['form_user']
            user.username = form.cleaned_data['form_user']
            user.save()
            return redirect('/listUser')
        else:
            print(form.errors)

    return redirect('/listUser')

@login_required
def login_view(request):
    return redirect('home')