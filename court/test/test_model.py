from django.test import TestCase
from court.models import Court, Reservation
from django.contrib.auth.models import User

diccionario_pista ={
    'name':'nombre','width':'100.00','length':'100.00','description':'descripcion',
    'avaible':'Si','image':'imagen','price':'200.00',
}

diccionario_reserva ={
    'date':'01/01/2017','hour':'17:00',
    'duration':'02:00','cost':'100.00',
}

# models test
class CourtTest(TestCase):

    def create_court(self):
        return Court.objects.create(**diccionario_pista)

    def test_court_creation(self):
        c = self.create_court()
        self.assertTrue(isinstance(c, Court))
        self.assertEqual(c.__unicode__(), diccionario_pista['name'])
        
class ReservationTest(TestCase):

    def create_reservation(self):
        usuario = User.objects.create(username='usuario', password='usuario', email='usuario@gmail.com')
        pista = Court.objects.create(**diccionario_pista)
        return Reservation.objects.create(user=usuario, court=pista, **diccionario_reserva)

    def test_reservation_creation(self):
        r = self.create_reservation()
        self.assertTrue(isinstance(r, Reservation))
        self.assertEqual(r.__unicode__(), r.user.username + '->' + r.court.name)
