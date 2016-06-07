from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

class Classroom(models.Model):
    """Represents a Classroom existing in the gym.
    :idClassroom: The primary key for the classroom.
    :name: The name for the classroom. Must be unique.
    :width: The total width of the classroom in meters.
    :length: The total length of the classroom in meters.
    :avaible: Represents the avaibility of classroom at the moment.
    :description: More information about the classroom.
    :image: A image of the classroom.
    :capacity: The number of people that can be inside in a moment.
    """
    idClassroom = models.AutoField(
        primary_key=True, 
        verbose_name='Aula',
        db_column='idClassroom',
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        default='',
        verbose_name='Nombre',
        db_column='name',
        help_text='Solo letras, numeros y espacios.',
        validators=[
            RegexValidator(
                regex='^([0-9a-zA-Z][, .:]*){1,200}$',
                message='Solo letras, puntuacion y numeros, maximo 200.', 
                code='invalid_name',
            )
        ],
    )
    width = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        verbose_name='Ancho', 
        db_column='width',
        help_text='1 a 5 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,5}\.[0-9]{1,2})|([0-9]{1,5}))$',
                message='1 a 5 parte entera y 2 parte decimal.', 
                code='invalid_width',
            )
        ],
    )
    length = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Largo',
        db_column='length',
        help_text='1 a 5 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,5}\.[0-9]{1,2})|([0-9]{1,5}))$',
                message='1 a 5 parte entera y 2 parte decimal.', 
                code='invalid_length',
            )
        ],
    )
    avaible = models.CharField(
        max_length=2,
        verbose_name='Disponible',
        db_column='avaible',
        validators=[
            RegexValidator(
                regex='^(Si|No)$',
                message='Solo si o No.', 
                code='invalid_avaible',
            )
        ],
    )
    description = models.TextField(
        verbose_name='Descripcion',
        db_column='description',
        help_text='Solo letras, numeros y espacios.',
        default='',
        validators=[
            RegexValidator(
                regex='^([0-9a-zA-Z][, .:]*){1,500}$',
                message='Solo letras, puntuacion y numeros, maximo 500.', 
                code='invalid_description',
            )
        ],
    )
    image = models.ImageField(
        upload_to='classroom/',
        verbose_name='Imagen',
        db_column='image',
        help_text='jpg,bmp,svg o png.',
    )
    capacity = models.CharField(
        max_length=2,
        verbose_name='Capacidad', 
        db_column='capacity',
        help_text='Minimo 1, maximo 99.', 
        default=1,
        validators=[
            RegexValidator(
                regex='^([1-9]|[1-9][0-9])$',
                message='Entre 1 y 99.', 
                code='invalid_capacity',
            )
        ],
    )

    class Meta:
        db_table = 'Classroom'
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __unicode__(self):
        return self.name

class Course(models.Model):
    """Represents a Course which is teach in the gym.
    :idCourse: The primary key for the course.
    :name: The name of the course. Must be unique.
    :description: More information about the course.
    :day: Day of the week for the course.
    :hour: Starting hour for the course.
    :duration: The duration of one class of the course.
    :cost: The total cost of the course.
    """
    idCourse = models.AutoField(
        primary_key=True,
        verbose_name='Curso',
        db_column='idCourse',
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        default='',
        verbose_name='Nombre',
        db_column='name',
        help_text='Solo letras, numeros y espacios.',
        validators=[
            RegexValidator(
                regex='^([0-9a-zA-Z][, .:]*){1,200}$',
                message='Solo letras, puntuacion y numeros, maximo 200.', 
                code='invalid_name',
            )
        ],
    )
    description = models.TextField(
        verbose_name='Descripcion',
        db_column='description',
        help_text='Solo letras, numeros y espacios.',
        default='',
        validators=[
            RegexValidator(
                regex = '^([0-9a-zA-Z][, .:]*){1,500}$',
                message = 'Solo letras, puntuacion y numeros, maximo 500.', 
                code = 'invalid_description',
            )
        ],
    )
    days = (('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'),
            ('Jueves', 'Jueves'), ('Viernes', 'Viernes'),)
    day = models.CharField(
        max_length=100, 
        choices=days, 
        default='Lunes',
        verbose_name='Dia', 
        db_column='day',
    )
    hour = models.CharField(
        verbose_name='Hora',
        db_column='hour',
        help_text='09:00 a 20:00 horas exactas.',
        default='09:00',
        max_length=5,
        validators=[
            RegexValidator(
                regex='^(09|1[0-9]|20):00$',
                message='de 09:00 a 20:00, horas exactas.', 
                code='invalid_hour',
            )
        ],
    )
    duration = models.CharField(
        verbose_name='Duracion',
        db_column='duration',
        help_text='01-09 horas:00.',
        default='01:00',
        max_length=5,
        validators=[
            RegexValidator(
                regex='^(0[1-9]):00$',
                message='hh:mm,mm = 01:00-09:00 min 01:00 max 09:00 horas.', 
                code='invalid_duration',
            )
        ],
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Coste',
        db_column='cost',
        help_text='1 a 8 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,8}\.[0-9]{1,2})|([0-9]{1,8}))$',
                message='1 a 8 parte entera y 2 parte decimal.', 
                code='invalid_cost',
            )
        ],
    )

    class Meta:
        db_table = 'Course'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __unicode__(self):
        return self.name

class Participation(models.Model):
    """Represents a participation of a user in a course.
    :idParticipation: The primary key for the participation.
    :user: The user who participates in the course. FK for User.
    :course: The course to be participate in. FK for Course.
    """
    idParticipation = models.AutoField(
        primary_key=True,
        verbose_name='Participacion',
        db_column='idParticipation',
    )
    user = models.ForeignKey(
        User,
        related_name='participation_user',
        verbose_name='Usuario',
        db_column='user',
    )
    course = models.ForeignKey(
        Course,
        related_name='participation_course',
        verbose_name='Curso',
        db_column='course',
    )
    
    class Meta:
        db_table = 'Participation'
        verbose_name = 'Participacion'
        verbose_name_plural = 'Participaciones'

    def __unicode__(self):
        return self.user.username + '->' + self.course.name

class Place(models.Model):
    """Represents the place where the course is teach.
    :idPlace: The primary key for the place.
    :classroom: The classroom where is teach the course. FK for Classroom.
    :course: The course to be teach in. FK for Course.
    """
    idPlace = models.AutoField(
        primary_key=True,
        verbose_name='Lugar',
        db_column='idPlace',
    )
    classroom = models.ForeignKey(
        Classroom,
        related_name='place_classroom',
        verbose_name='Clase',
        db_column='classroom',
    )
    course = models.ForeignKey(
        Course,
        related_name='place_course',
        verbose_name='Curso',
        db_column='course',
    )
    
    class Meta:
        db_table = 'Place'
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def __unicode__(self):
        return self.classroom.name + '->' + self.course.name