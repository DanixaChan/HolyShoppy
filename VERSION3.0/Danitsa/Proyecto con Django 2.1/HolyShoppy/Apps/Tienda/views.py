from django.shortcuts import redirect,render
from .models import Usuario,Pago,Detalleproducto,Producto
from .forms import UsuarioForm

def home(request): 
    return render(request, 'index.html')

def registro(request):
    return render(request, 'usuarios/registro.html')

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