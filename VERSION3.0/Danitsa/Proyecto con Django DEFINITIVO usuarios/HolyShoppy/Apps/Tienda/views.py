from django.shortcuts import redirect,get_object_or_404,render,HttpResponseRedirect
from .models import Usuario,Pago,Detalleproducto,Producto
from django.contrib import messages
from .forms import UsuarioForm,LoginForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# def sign_in(request):

#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request,'users/login.html', {'form': form})
    
#     elif request.method == 'POST':
#         form = LoginForm(request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user = authenticate(request,username=username,password=password)
#             if user:
#                 login(request, user)
#                 messages.success(request,f'Hi {username.title()}, welcome back!')
#                 return redirect('posts')
        
#         # either form not valid or user is not authenticated
#         messages.error(request,f'Invalid username or password')
#         return render(request,'users/login.html',{'form': form})
    
    
        
# def sign_out(request):
#     logout(request)
#     messages.success(request,f'You have been logged out.')
#     return redirect('login')        



# def login(request):
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             return redirect('posts')
        
#         form = LoginForm()
#         return render(request,'login.html', {'form': form})
    
#     elif request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 # Redirigir al usuario a la página deseada después del inicio de sesión
#                 return redirect('home')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista
#     return render(request, 'login.html', {'form': form})




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