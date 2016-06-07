from django.db import models
from django.core.validators import RegexValidator

class Machine(models.Model):
    """Represents a Machine existing in the gym.
    :idMachine: The primary key for the machine.
    :name: The name for the machine. Must be unique.
    :description: More information about the machine.
    :image: A image of the machine.
    :quantity: The number of this machine in the gym.
    """
    idMachine = models.AutoField(
        primary_key=True, 
        verbose_name='Maquina', 
        db_column='idMachine',
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
        upload_to='machine/', 
        verbose_name='Imagen',
        db_column='image', 
        help_text='jpg,bmp,svg o png.',
    )
    quantity = models.CharField(
        max_length=2, 
        verbose_name='Cantidad', 
        db_column='quantity',
        help_text='Minimo 1, maximo 99.', 
        default=1,
        validators=[
            RegexValidator(
                regex='^([1-9]{1,1}|[1-9]{1,1}[0-9]{1,1})$',
                message='Entre 1 y 99.', 
                code='invalid_quantity',
            )
        ],
    )

    class Meta:
        db_table = 'Machine'
        verbose_name = 'Maquina'
        verbose_name_plural = 'Maquinas'

    def __unicode__(self):
        return self.name


class Exercise(models.Model):
    """Represents a Exercise for a machine.
    :idExercise: The primary key for the exercise.
    :machine: The machine where exercise is done. FK for Machine.
    :name: The name of the exercise. Must be unique.
    :image: A image of the exercise.
    :zone: The zone of the body that is affected by the exercise.
    """
    idExercise = models.AutoField(
        primary_key=True, 
        verbose_name='Ejercicio', 
        db_column='idExercise',
    )
    machine = models.ForeignKey(
        Machine, 
        related_name='exercise_machine', 
        verbose_name='Maquina',
        db_column='machine',
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
    image = models.ImageField(
        upload_to='exercise/', 
        verbose_name='Imagen',
        db_column='image', 
        help_text='jpg,bmp,svg o png.',
    )
    zones = ( ('Pecho', 'Pecho'), ('Espalda', 'Espalda'),
              ('Brazos', 'Brazos'), ('Piernas', 'Piernas'),)
    zone = models.CharField(
        max_length=100, 
        choices=zones, 
        default='Pecho',
        verbose_name='Zona', 
        db_column='zone',
    )

    class Meta:
        db_table = 'Exercise'
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __unicode__(self):
        return self.machine.name + '->' + self.name


class Programm(models.Model):
    """Represents a Programm of exercises.
    :idProgramm: The primary key for the programm.
    :exercise: The exercises inside the programm. FK for exercise.
    :name: The name of the programm. Must be unique.
    :quantity: The quantity per serie of the exercise.
    :series: The number of series of the exercise.
    :rest: The rest bettwen series.
    """
    idProgramm = models.AutoField(
        primary_key=True, 
        verbose_name='Reserva', 
        db_column='idReservation',
    )
    exercise = models.ForeignKey(
        Exercise, 
        related_name='programm_exercise', 
        verbose_name='Ejercicio',
        db_column='exercise',
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
    quantity = models.CharField(
        max_length=2, 
        verbose_name='Cantidad', 
        db_column='quantity',
        help_text='Minimo 1, maximo 99.', 
        default=1,
        validators=[
            RegexValidator(
                regex='^([1-9]{1,1}|[1-9]{1,1}[0-9]{1,1})$',
                message='Entre 1 y 99.', 
                code='invalid_quantity',
            )
        ],
    )
    series = models.CharField(
        max_length=2,
        verbose_name='Series', 
        db_column='series',
        help_text='Minimo 1, maximo 15.', 
        default=1,
        validators=[
            RegexValidator(
                regex='^([1-9]{1,1}|[1][0-5]{1,1})$',
                message='Entre 1 y 15.', 
                code='invalid_series',
            )
        ],
    )
    rest = models.CharField(
        max_length=2,
        verbose_name='Descanso', 
        db_column='rest',
        help_text='Minimo 1, maximo 15.', 
        default=1,
        validators=[
            RegexValidator(
                regex='^([1-9]{1,1}|[1][0-5]{1,1})$',
                message='Entre 0 y 15.', 
                code='invalid_rest',
            )
        ],
    )

    class Meta:
        db_table = 'Programm'
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def __unicode__(self):
        return self.name


class Planification(models.Model):
    """Represents a Planification of programms.
    :idPlanification: The primary key for the planification.
    :programm: The programms inside the planification. FK for programm.
    :name: The name of the planification. Must be unique.
    :day: The day of the week for this planification.
    """
    idPlanification = models.AutoField(
        primary_key=True, 
        verbose_name='Planificacion', 
        db_column='idPlanification',
    )
    programm = models.ForeignKey(
        Programm, 
        related_name='planification_programm', 
        verbose_name='Programa',
        db_column='programm',
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
    days = (('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'),
            ('Jueves', 'Jueves'), ('Viernes', 'Viernes'),)
    day = models.CharField(
        max_length=100, 
        choices=days, 
        default='Lunes',
        verbose_name='Dia', 
        db_column='day',
    )

    class Meta:
        db_table = 'Planification'
        verbose_name = 'Planificacion'
        verbose_name_plural = 'Planificaciones'

    def __unicode__(self):
        return self.name
