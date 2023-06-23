from django.shortcuts import redirect,render
from .models import Usuario,Pago,Detalleproducto,Producto
from .forms import UsuarioForm

def home(request): 
    return render(request, 'index.html')

def registro(request):
    return render(request, 'usuarios/registro.html')

# def alumnosListV2(request):
#     #defino un objeto para trar el listado completo de alumnos desde la BD
#     #Alumno.objects.all() <=> 'Select * From Alumnos'
#     alumnos= Alumno.objects.all()
#     #cargo el objeto obtenido al contexto 
#     contexto={
#         'alumnos': alumnos
#     }
#     #agrego el contexto al retorno para que se vea en el template
#     return render(request, 'alumnos/alumnosListV2.html', contexto)

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
    return render(request, 'usuarios/registro.html', context)