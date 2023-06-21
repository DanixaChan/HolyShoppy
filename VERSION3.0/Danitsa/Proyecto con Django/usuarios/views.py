from django.shortcuts import render

from .forms import ProductoForm,UsuarioForm,RegistroForm
from .models import Producto,Usuario,Pago,Detalleproducto

# Create your views here.
def index(request):
    return render(request,'usuarios/index.html')

def usuariosList(request):

    usuarios = Usuario.objects.all()
    contexto={
        'usuarios': usuarios
    }
    return render(request, 'usuarios/registro.html', contexto)

def usuariosAdd(request):
    #el view entrega el form al template
    context={'form' : UsuarioForm()}
    #verifico que la petición sea post
    if request.method=='POST':
        #con request recupero la información del formulario
        formulario=UsuarioForm(request.POST, files=request.FILES)
        #valido el formulario
        if formulario.is_valid:
            #lo guardo
            formulario.save()
            context={'mensaje':"Has sido registrado con éxito"}
    return render(request, 'usuarios/registro.html', context)

def SelectView(request):
    pagos = Pago.objects.all()  # Obtén los métodos de pago desde la base de datos
    print(pagos)  # Imprimir los registros en la consola para verificar
    form = UsuarioForm()
    return render(request, 'registro.html', {'form': form, 'pagos': pagos})

def registro_view(request):
    pagos = Pago.objects.all()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.metodo_pago = request.POST['form_payment_card']
            form.save()
            # Lógica adicional después de guardar el formulario
    else:
        form = RegistroForm()

    context = {'form': form, 'pagos': pagos}
    return render(request, 'registro.html', context)