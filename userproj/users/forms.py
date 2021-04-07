from django import forms
from users.models import Usuarios,Comments,UserProfileData
from django.core import validators
from django.contrib.auth.models import User


class UserForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


def check_a(valor):
    if valor[0] != 'A':
        raise forms.ValidationError("El nombre tiene que comenzar con A")

class Commentscambiado(forms.Form):
    Nombre = forms.CharField(validators=[check_a])
    Comment = forms.CharField(max_length=200, widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


class Comment(forms.ModelForm):
    class Meta():
        model = Comments
        fields = "__all__"



class RegisterForm(forms.ModelForm):
    class Meta():
        model = Usuarios
        fields = "__all__"

class UserFormulario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileDataForm(forms.ModelForm):
    profile_URL = forms.URLField(required=False)
    profile_image = forms.ImageField(required=False)

    class Meta():
        model = UserProfileData
        fields = ('profile_URL', 'profile_image')
