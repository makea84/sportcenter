# encoding:utf-8
from django.forms import ModelForm, Textarea, TextInput
from .models import Machine, Exercise, Programm, Planification
from django.forms.widgets import Select

zones = ( ('Pecho', 'Pecho'), ('Espalda', 'Espalda'),
              ('Brazos', 'Brazos'), ('Piernas', 'Piernas'),)

days = (('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'),
            ('Jueves', 'Jueves'), ('Viernes', 'Viernes'),)

class MachineForm(ModelForm):
    """Represents a form for a Machine.
    :name: The name for the machine. Must be unique.
    :description: More information relevant of the machine.
    :quantity: The number of this machine.
    :image: A image of the machine.
    """
    class Meta:
        model = Machine
        fields =('name', 'description', 'quantity', 'image')
        labels ={
            'name':'Nombre', 'description':'Descripcion',
            'quantity':'Cantidad', 'image':'Imagen',
        },
        help_texts = {
            'name':'Solo letras, numeros y espacios.',
            'description':'Solo letras, numeros y espacios.',
            'quantity':'Dos digitos maximo.',    
        },
        error_messages = {
            'name': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 200.',
                'required':'Campo obligatorio.',
            },
            'description': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 500.',
                'required':'Campo obligatorio.',
            },
            'quantity': {
                'min_value':'Valor minimo 1.',
                'max_value':'Valor maximo 99',
                'required':'Campo obligatorio.',
                'invalid':'Cantidad no valida.'
            },
        },
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Longitud entre 1 y 200.'}),
            'description': Textarea(attrs={'placeholder': 'Longitud entre 1 y 500.','rows':'2'}),
            'quantity': TextInput(
                            attrs={
                                'placeholder': 'Entre 1-99.',
                                'type':'number',
                                'min':'1',
                                'max':'99',
                                'step':'1'
                            }
            ),
        }
        
class ExerciseForm(ModelForm):
    """Represents a form for a  Exercise.
    :name: The name of the exercise. Must be unique.
    :machine: The machine asociated with the exercise.
    :zone: The zone of the body affected.
    :image: A image of the exercise.
    """
    class Meta:
        model = Exercise
        fields =('name', 'machine', 'zone', 'image')
        labels ={
            'name':'Nombre', 'machine':'Maquina',
            'zone':'Zona', 'image':'Imagen',
        },
        help_texts = {
            'name':'Solo letras, numeros y espacios.',   
        },
        error_messages = {
            'name': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 200.',
                'required':'Campo obligatorio.',
            },
        },
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Longitud entre 1 y 200.'}),
            'zone': Select(attrs={'placeholder': 'Longitud entre 1 y 200.'}, choices=zones),
        }

class ProgrammForm(ModelForm):
    """Represents a form for a Programm.
    :name: The name of the programm. Must be unique.
    :exercise: The exercise asociate to the programm.
    :series: The number of series.
    :quantity: The quantity per serie.
    :rest: The rest bettwen series.
    """
    class Meta:
        model = Programm
        
        fields =('name','series', 'quantity', 'rest','exercise')
        labels ={
            'name':'Nombre', 'quantity':'Cantidad', 'image':'Imagen',
            'series':'Series', 'rest':'Descanso', 'exercise':'Ejercicio'
        },
        help_texts = {
            'name':'Solo letras, numeros y espacios.',
            'series':'Dos digitos maximo.',
            'quantity':'Dos digitos maximo.', 
            'rest':'Entre 1-15 minutos',   
        },
        error_messages = {
            'name': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 200.',
                'required':'Campo obligatorio.',
            },
            'quantity': {
                'min_value':'Valor minimo 1.',
                'max_value':'Valor maximo 99.',
                'required':'Campo obligatorio.',
                'invalid':'Cantidad no valida.'
            },
            'series': {
                'min_value':'Valor minimo 1.',
                'max_value':'Valor maximo 15.',
                'required':'Campo obligatorio.',
                'invalid':'Cantidad no valida.'
            },
            'rest': {
                'min_value':'Valor minimo 1.',
                'max_value':'Valor maximo 15.',
                'required':'Campo obligatorio.',
                'invalid':'Cantidad no valida.'
            },
        },
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Longitud entre 1 y 200.'}),
            'quantity': TextInput(
                            attrs={
                                'placeholder': 'Entre 1-99.',
                                'type':'number',
                                'min':'1',
                                'max':'99',
                                'step':'1'
                            }
            ),
            'series': TextInput(
                        attrs={
                            'placeholder': 'Entre 1-15.',
                            'type':'number',
                            'min':'1',
                            'max':'15',
                            'step':'1'
                        }
            ),
            'rest': TextInput(
                        attrs={
                            'placeholder': 'Entre 1-15.',
                            'type':'number',
                            'min':'1',
                            'max':'15',
                            'step':'1'
                        }
            ),
        }

class PlanificationForm(ModelForm):
    """Represents a form for a Planification.
    :name: The name of the planification. Must be unique.
    :programm: The programm in planification.
    :day: The day of the week.
    """
    class Meta:
        model = Planification
        fields =('name', 'day', 'programm')
        labels ={
            'name':'Nombre', 'programm':'Programa', 'day':'Dia',
        },
        help_texts = {
            'name':'Solo letras, numeros y espacios.',
        },
        error_messages = {
            'name': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 200.',
                'required':'Campo obligatorio.',
            },
        },
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Longitud entre 1 y 200.'}),
            'date': Select(attrs={'placeholder': 'Longitud entre 1 y 200.'}, choices=days),
        }

class PlanForm(ModelForm):
    """Represents a form for a Planification.
    :name: The name of the planification. Must be unique.
    :programm: The programm in planification.
    :day: The day of the week.
    """
    class Meta:
        model = Planification
        fields =('programm',)
        labels ={
             'programm':'Programa',
        },