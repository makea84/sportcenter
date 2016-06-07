from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

class Court(models.Model):
    """Represents a Court that exists in the gym.
    :idCourt: The primary key for the court.
    :name: The name for the court. Must be unique.
    :width: The total width of court in meters.
    :length: The total length of court in meters.
    :avaible: Represent the avaibility of court at the moment.
    :description: More information about the court.
    :image: A image of the court.
    :price: The price for rent the court during a hour.
    """
    idCourt = models.AutoField(
        primary_key=True, 
        verbose_name='Pista',
        db_column='idCourt',
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
                message='Solo Si o No.', 
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
        upload_to='court/',
        verbose_name='Imagen',
        db_column='image',
        help_text='jpg,bmp,svg o png.',
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Precio',
        db_column='price',
        help_text='1 a 3 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,3}\.[0-9]{1,2})|([0-9]{1,3}))$',
                message='1 a 3 parte entera y 2 parte decimal.', 
                code='invalid_price',
            )
        ],
    )

    class Meta:
        db_table = 'Court'
        verbose_name = 'Pista'
        verbose_name_plural = 'Pistas'

    def __unicode__(self):
        return self.name


class Reservation(models.Model):
    """Represents a Reservation for a court.
    :idReservation: The primary key for the reservation.
    :user: The user who reserve the court. FK for User.
    :court: The court which is going to be reserve. FK for Court.
    :date: The date of the reservation.
    :hour: The hour of the reservation.
    :duration: Duration of the reservation.
    :cost: The total cost for the reservation.
    """
    idReservation = models.AutoField(
        primary_key=True,
        verbose_name='Reserva',
        db_column='idReservation',
    )
    user = models.ForeignKey(
        User,
        related_name='reservation_user',
        verbose_name='Usuario',
        db_column='user',
    )
    court = models.ForeignKey(
        Court,
        related_name='reservation_court',
        verbose_name='Pista',
        db_column='court',
    )
    date = models.CharField(
        verbose_name='Fecha',
        db_column='date',
        help_text='aaaa-mm-dd.',
        default='2016-06-10',
        max_length=10,
        validators=[
            RegexValidator(
                regex='^([2-9][0-9]{3})\-(0[1-9]|1[0-2])\-(0[1-9]|[1|2][0-9]|[3][0|1])$',
                message='aaaa-mm-dd.', 
                code='invalid_date',
            )
        ],
    )
    hour = models.CharField(
        verbose_name='Hora',
        db_column='hour',
        help_text='09:00 a 20:00 horas exactas.',
        default='09:00',
        max_length=5,
        validators=[
            RegexValidator(
                regex='^((09|1[0-9]|20):00)$',
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
        db_table = 'Reservation'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __unicode__(self):
        return self.user.username + '->' + self.court.name
