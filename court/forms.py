# encoding:utf-8
from django.forms import ModelForm, Textarea, TextInput
from .models import Court, Reservation
from django.forms.widgets import Select

yesno = (('Si', 'Si'), ('No', 'No'),)

class CourtForm(ModelForm):
    """Represents a form for a Court.
    :name: The name for the court. Must be unique.
    :width: The total width of court in meters.
    :length: The total length of court in meters.
    :avaible: Represent the avaibility of court at the moment.
    :description: Aditional information about the court.
    :price: The price for rent the court.
    :image: A image of the court.
    """
    class Meta:
        model = Court
        fields =('name', 'width', 'length', 'avaible', 'description', 'price', 'image')
        labels ={
            'name':'Nombre', 'width':'Ancho', 'length':'Largo', 'description':'Descripcion',
            'price':'Precio', 'image':'Imagen', 'avaible':'Disponible',
        },
        help_texts = {
            'name':'Solo letras, numeros y espacios.',
            'width':'Cantidad expresada en metros.',
            'length':'Cantidad expresada en metros.',
            'description':'Solo letras, numeros y espacios.',
            'price':'Precio expresado en euros.',
            'avaible':'Esta disponible, Si o No.',     
        },
        error_messages = {
            'name': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 200.',
                'required':'Campo obligatorio.',
            },
            'width': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.',
            },
            'length': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.',
            },
            'avaible': {
                'required':'Campo obligatorio.',
            },
            'description': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 500.',
                'required':'Campo obligatorio.',
            },
            'price': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.',
            },
        },
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Longitud entre 1 y 200.'}),
            'width': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-99999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'99999.99',
                            'step':'0.01'
                        }
            ),
            'length': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-99999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'99999.99',
                            'step':'0.01'
                        }
            ),
            'avaible': Select(attrs={'placeholder': 'Si o No.'}, choices=yesno),
            'description': Textarea(attrs={'placeholder': 'Longitud entre 1 y 500.','rows':'2'}),
            'price': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'999.99',
                            'step':'0.01'
                        }
            ),
        }
        
class ReservationForm(ModelForm):
    """Represents a form for a Reservation.
    :date: The date of the reservation.
    :hour: The hour of the reservation.
    :duration: Duration of the reservation.
    :cost: The cost for the reservation.
    :user: The user who reserve.
    :court: The court to reserve.
    """
    class Meta:
        model = Reservation
        fields =('date', 'hour', 'duration', 'cost', 'user','court')
        labels ={
            'date':'Fecha', 'hour':'Hora', 'duration':'Duracion', 'cost':'Coste',
            'user':'Usuario', 'court':'Pista',
        },
        help_texts = {
            'date':'Formato dd/mm/aaaa.',
            'hour':'Formato hh:mm.',
            'duration':'Formato hh:mm.',
            'cost':'Coste expresado en euros.',
        },
        error_messages = {
            'date': {
                'invalid':'Fecha no valida.',
                'required':'Campo obligatorio.',
            },
            'hour': {
                'invalid':'Hora no valida.', 
                'required':'Campo obligatorio.'
            },
            'duration': {
                'invalid':'Duracion no valida.', 
                'required':'Campo obligatorio.'
            },
            'cost': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.'
            },
            'user': {
                'required':'Campo obligatorio.'
            },
        },
        widgets = {
            'date': TextInput(
                        attrs={
                            'placeholder': 'dd-mm-aaaa.',
                            'type':'date',
                            'min':'2016-06-06'
                        }
            ),
            'duration': TextInput(
                        attrs={
                            'placeholder': 'Entre 01:00-09:00. Horas exactas.',
                            'type':'time',
                            'min':'01:00',
                            'max':'09:00'
                        }
            ),
            'hour': TextInput(
                        attrs={
                            'placeholder': 'Entre 09:00-20:00. Horas exactas.',
                            'type':'time',
                            'min':'09:00',
                            'max':'20:00',
                            'step':'01:00'
                        }
            ),
            'cost': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-99999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'99999.99',
                            'step':'0.01'
                        }
            ),
        }

class ReservateForm(ModelForm):
    """Represents a form for a Reservation.
    :date: The date of the reservation.
    :hour: The hour of the reservation.
    :duration: Duration of the reservation.
    :cost: The cost for the reservation.
    :user: The user who reserve.
    :court: The court to reserve.
    """
    class Meta:
        model = Reservation
        fields =('date', 'hour', 'duration', 'cost')
        labels ={
            'date':'Fecha', 'hour':'Hora', 'duration':'Duracion', 'cost':'Coste', 'court':'Pista',
        },
        help_texts = {
            'date':'Formato dd/mm/aaaa.',
            'hour':'Formato hh:mm.',
            'duration':'Formato hh:mm.',
            'cost':'Coste expresado en euros.',
        },
        error_messages = {
            'date': {
                'invalid':'Fecha no valida.',
                'required':'Campo obligatorio.',
            },
            'hour': {
                'invalid':'Hora no valida.', 
                'required':'Campo obligatorio.'
            },
            'duration': {
                'invalid':'Duracion no valida.', 
                'required':'Campo obligatorio.'
            },
            'cost': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.'
            },
        },
        widgets = {
            'date': TextInput(
                        attrs={
                            'placeholder': 'dd-mm-aaaa.',
                            'type':'date',
                            'min':'2016-06-06'
                        }
            ),
            'duration': TextInput(
                        attrs={
                            'placeholder': 'Entre 01:00-09:00. Horas exactas.',
                            'type':'time',
                            'min':'01:00',
                            'max':'09:00'
                        }
            ),
            'hour': TextInput(
                        attrs={
                            'placeholder': 'Entre 09:00-20:00. Horas exactas.',
                            'type':'time',
                            'min':'09:00',
                            'max':'20:00',
                            'step':'01:00'
                        }
            ),
            'cost': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-99999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'99999.99',
                            'step':'0.01',
                            'readonly':'true'
                        }
            ),
        }
