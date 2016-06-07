# encoding:utf-8
from django.forms import ModelForm, Textarea, TextInput
from .models import Classroom, Course, Participation, Place
from django.forms.widgets import Select

days = (('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'),
            ('Jueves', 'Jueves'), ('Viernes', 'Viernes'),)
yesno = (('Si', 'Si'), ('No', 'No'),)

class ClassroomForm(ModelForm):
    """Represents a form for classroom.
    :name: The name for the classroom. Must be unique.
    :width: The width of the classroom in meters.
    :length: The length of the classroom in meters.
    :avaible: Represents the avaibility of classroom at the moment.
    :description: Some aditional information of the classroom.
    :capacity: Total amount of people in the classroom in a moment.
    :image: A image of the classroom.
    """
    class Meta:
        model = Classroom
        fields =('name', 'width', 'length', 'avaible', 'description', 'capacity', 'image')
        labels ={
            'name':'Nombre', 'width':'Ancho', 'length':'Largo', 'description':'Descripcion',
            'capacity':'Capacidad', 'image':'Imagen','avaible':'Disponible',
        },
        help_texts = {
            'name':'Solo letras, numeros y espacios.',
            'width':'Cantidad expresada en metros.',
            'length':'Cantidad expresada en metros.',
            'description':'Solo letras, numeros y espacios.',
            'capacity':'Capacidad total de personas.',
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
            'capacity': {
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
            'capacity': TextInput(
                        attrs={
                            'placeholder': 'Entre 1-99.',
                            'type':'number',
                            'min':'1',
                            'max':'99',
                            'step':'1'
                        }
            ),
        }
        
class CourseForm(ModelForm):
    """Represents a form for a course.
    :name: The name of the course. Must be unique.
    :description: Some aditional information of the course.
    :day: Day of the week when the course is offer.
    :hour: Hour of the day when the course is offer.
    :duration: Time spended in a session.
    :cost: Cost of the course. 
    """
    class Meta:
        model = Course
        fields =('name', 'description','day', 'hour', 'duration', 'cost')
        labels ={
            'day':'Dia', 'hour':'Hora', 'duration':'Duracion', 'cost':'Coste',
            'name':'Nombre', 'description':'Descripcion',
        },
        help_texts = {
            'date':'Formato dd/mm/aaaa.',
            'hour':'Formato hh:mm.',
            'duration':'Formato hh:mm.',
            'cost':'Coste expresado en euros.',
            'name':'Solo letras, numeros y espacios.',
            'description':'Solo letras, numeros y espacios.',
        },
        error_messages = {
            'day': {
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
            'description': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 500.',
                'required':'Campo obligatorio.',
            },
            'name': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 200.',
                'required':'Campo obligatorio.',
            },
        },
        widgets = {
            'day': Select(attrs={'placeholder':'Dia de la semana Lunes-Viernes.'},
                               choices=days),
            'duration': TextInput(
                            attrs={
                                'placeholder': 'Entre 01:00-09:00. Horas exactas.',
                                'type':'time',
                                'min':'01:00',
                                'max':'09:00',
                                'step':'01:00'
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
            'name': TextInput(attrs={'placeholder': 'Longitud entre 1 y 200.'}),
            'description': Textarea(attrs={'placeholder': 'Longitud entre 1 y 500.','rows':'2'}),
        }
        
class ParticipationForm(ModelForm):
    """Represents a form for a participation of a user in a course.
    :user: The user who is going to be in the course.
    :course: The course to participate.
    """
    class Meta:
        model = Participation
        fields =('user', 'course',)
        labels ={
            'user':'Usuario', 'course':'Curso',
        },
        error_messages = {
            'user': {
                'invalid':'Usuario no valido.',
                'required':'Campo obligatorio.',
            },
            'course': {
                'invalid':'Curso no valido.', 
                'required':'Campo obligatorio.'
            }, 
        }

class PlaceForm(ModelForm):
    """Represents a form for a place where the course is going to be.
    :classroom: The classroom where is going to be the course.
    :course: The course that is celebrate in the classroom.
    """
    class Meta:
        model = Place
        fields =('classroom', 'course',)
        labels ={
            'classroom':'Aula', 'course':'Curso',
        },
        error_messages = {
            'classroom': {
                'invalid':'Clase no valida.',
                'required':'Campo obligatorio.',
            },
            'course': {
                'invalid':'Curso no valido.', 
                'required':'Campo obligatorio.'
            }, 
        }
