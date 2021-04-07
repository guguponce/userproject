from django.shortcuts import render
from users.models import Usuarios,Comments,UserProfileData
from django.http import HttpResponse
from users.forms import Comment,UserFormulario,UserProfileDataForm
from users import forms

#LogIn
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    contenido = {'INSERT_HOME':"Está en la página principal"}
    return render(request, 'index.html', context=contenido)


def users(request):
    # cont_user = {'INSERT_USER':'Esta es la lista de usuarios:'}
    # return render(request, 'users.html', context=cont_user)
    #
    email_list = Usuarios.objects.order_by('email')
    email_insert = {"users":email_list}
    return render(request, 'users.html', context=email_insert)

def formulario(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print('Validation succeeded')
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Texto: '+form.cleaned_data['text'])



    return render(request,'formulario.html',{'form':form})

def Comments(request):
    comment_form = forms.Comment()
    if request.method == 'POST':
        comment_form = forms.Comment(request.POST)

        if comment_form.is_valid():
            print('Valido')
            print('Nombre: '+comment_form.cleaned_data['nombre'])
            print('Comentario: '+comment_form.cleaned_data['comentario'])
            comment_form.save(commit=True)
            return index(request)
        else:
            print('Comentario invalido')
    return render(request, 'comentario.html', {'formulario':comment_form})

def Registered(request):
    return render(request, 'regThanks.html')

def Registro(request):

    registrado = False

    if request.method == 'POST':
        userform = UserFormulario(data=request.POST)
        registro = UserProfileDataForm(data=request.POST)

        if userform.is_valid() and registro.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = registro.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()

            registrado = True
        else:
            print(userform.errors,registro.errors)
    else:
        userform = UserFormulario()
        registro = UserProfileDataForm()

    return render(request, 'segundoregistro.html', {'userform':userform,
                                                    'registro':registro,
                                                    'registrado':registrado})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        cuenta = authenticate(username=username,password=password)
###################################################################
        if cuenta:
            if cuenta.is_active:
                login(request,cuenta)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Su cuenta no esta activa')
        else:
            return HttpResponse('Usuario y/o Contraseña inválido/s')
            print('Usuario: {} Contraseña: {}'.format(username,password))
    else:
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
