#encoding:utf-8
from django import forms

          
class UserAppForm(forms.Form):
    """Represents a form for a User of the application.
    :user: The user existing in the application. FK for User.
    :name: The real name of the user.
    :dni: The dni of the user.
    """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Longitud entre 1 y 200.'}
        ),
        label="Nombre",
        help_text="Solo letras y espacios.",
        min_length=1,
        max_length=200,
        error_messages={
            'min_length':'Longitud minima 1',
            'max_length':'Longitud maxima 200',
            'required':'Campo obligatorio',
        },
    )
    dni = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Longitud 8 numeros, guion y 1 letra.'}
        ),
        label="D.N.I.",
        help_text="Solo 8 numeros, un guion y una letra mayuscula.",
        min_length=10,
        max_length=10,
        error_messages={
            'min_length':'Longitud minima 10',
            'max_length':'Longitud maxima 10',
            'required':'Campo obligatorio',
        },
    )

class UserForm(forms.Form):
    """Represents a form for a User of Django.
    :username: The username for the user.
    :password: The password for the user.
    :email: The email of the user.
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Longitud entre 6 y 200.'}
        ),
        label="Nombre de usuario",
        help_text="Solo letras y numeros.",
        min_length=6,
        max_length=200,
        error_messages={
            'min_length':'Longitud minima 6',
            'max_length':'Longitud maxima 200',
            'required':'Campo obligatorio',
        },
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Longitud entre 6 y 200.'}
        ),
        label="Contraseña",
        help_text="Solo letras y numeros.",
        min_length=6,
        max_length=200,
        error_messages={
            'min_length':'Longitud minima 6',
            'max_length':'Longitud maxima 200',
            'required':'Campo obligatorio',
        },
    )
    email = forms.EmailField(
        label="E-mail",
        help_text="Solo letras, numeros, @, puntos y espacios.",
        min_length=6,
        max_length=200,
        error_messages={
            'min_length':'Longitud minima 6',
            'max_length':'Longitud maxima 200',
            'required':'Campo obligatorio',
        },
    )