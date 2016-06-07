from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

    
class UserApp(models.Model):
    """Represents a User of the application.
    :user: The user existing in the application. FK for User.
    :name: The real name of the user.
    :dni: The dni of the user.
    """
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=200, 
        unique=True, 
        verbose_name='Nombre',
        db_column='name', 
        help_text='Solo letras, numeros y espacios.', 
        default='',
        validators=[
            RegexValidator(
                regex='^([0-9a-zA-Z][, .:]*){1,200}$',
                message='Solo letras, puntuacion y numeros, maximo 200.', 
                code='invalid_name',
            )
        ],
    )
    dni = models.CharField(
        max_length=200,
        verbose_name='DNI',
        db_column='dni',
        unique=True,
        help_text='8 numeros, guion y letra.',
        validators=[
            RegexValidator(
                regex='^([0-9]{8}-[A-Z]{1,1})$',
                message='Solo letras, puntuacion y numeros, maximo 200.', 
                code='invalid_name',
            )
        ],
    )

    class Meta:
        db_table = 'UserApp'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __unicode__(self):
        return self.name