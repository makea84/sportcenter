from django.test import TestCase
from classroom.models import Classroom, Course, Place, Participation
from django.contrib.auth.models import User

diccionario_clase ={
    'name':'nombre','width':'100.00','length':'100.00','description':'descripcion',
    'avaible':'Si','image':'imagen','capacity':'01',
}

diccionario_curso ={
    'name':'nombre','day':'Lunes','hour':'17:00','description':'descripcion',
    'duration':'02:00','cost':'100.00',
}

# models test
class ClassroomTest(TestCase):

    def create_classroom(self):
        return Classroom.objects.create(**diccionario_clase)

    def test_classroom_creation(self):
        c = self.create_classroom()
        self.assertTrue(isinstance(c, Classroom))
        self.assertEqual(c.__unicode__(), diccionario_clase['name'])
        
class CourseTest(TestCase):

    def create_course(self):
        return Course.objects.create(**diccionario_curso)

    def test_course_creation(self):
        c = self.create_course()
        self.assertTrue(isinstance(c, Course))
        self.assertEqual(c.__unicode__(), diccionario_curso['name'])

class ParticipationTest(TestCase):

    def create_participation(self):
        usuario = User.objects.create(username='usuario', password='usuario', email='usuario@gmail.com')
        curso = Course.objects.create(**diccionario_curso)
        return Participation.objects.create(user=usuario, course=curso)

    def test_participation_creation(self):
        p = self.create_participation()
        self.assertTrue(isinstance(p, Participation))
        self.assertEqual(p.__unicode__(), p.user.username + '->' + p.course.name)

        
class PlaceTest(TestCase):

    def create_place(self):
        clase = Classroom.objects.create(**diccionario_clase)
        curso = Course.objects.create(**diccionario_curso)
        return Place.objects.create(classroom=clase, course=curso)

    def test_place_creation(self):
        p = self.create_place()
        self.assertTrue(isinstance(p, Place))
        self.assertEqual(p.__unicode__(), p.classroom.name + '->' + p.course.name)
