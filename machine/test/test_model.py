from django.test import TestCase
from machine.models import Machine, Exercise, Programm, Planification

diccionario_maquina ={'name':'nombre','description':'descripcion','image':'imagen','quantity':'01'}
diccionario_ejercicio ={'name':'nombre','image':'imagen','zone':'Brazos'}
diccionario_programa ={'name':'nombre','quantity':'10','series':'10','rest':'10'}
diccionario_planificacion ={'name':'nombre','day':'Lunes'}

# models test
class MachineTest(TestCase):

    def create_machine(self):
        return Machine.objects.create(**diccionario_maquina)

    def test_machine_creation(self):
        m = self.create_machine()
        self.assertTrue(isinstance(m, Machine))
        self.assertEqual(m.__unicode__(), diccionario_maquina['name'])
        
class ExerciseTest(TestCase):

    def create_exercise(self):
        maquina = Machine.objects.create(**diccionario_maquina)
        return Exercise.objects.create(machine=maquina, **diccionario_ejercicio)

    def test_exercise_creation(self):
        e = self.create_exercise()
        self.assertTrue(isinstance(e, Exercise))
        self.assertEqual(e.__unicode__(), e.machine.name + '->' + diccionario_ejercicio['name'])

class ProgrammTest(TestCase):

    def create_programm(self):
        maquina = Machine.objects.create(**diccionario_maquina)
        ejercicio = Exercise.objects.create(machine=maquina, **diccionario_ejercicio)
        programa = Programm.objects.create(**diccionario_programa)
        programa.exercise_set = ejercicio.pk
        programa.save()
        return programa

    def test_programm_creation(self):
        p = self.create_programm()
        self.assertTrue(isinstance(p, Programm))
        self.assertEqual(p.__unicode__(), p.name)
        
class PlanificationTest(TestCase):

    def create_planification(self):
        maquina = Machine.objects.create(**diccionario_maquina)
        ejercicio = Exercise.objects.create(machine=maquina, **diccionario_ejercicio)
        programa = Programm.objects.create(**diccionario_programa)
        programa.exercise_set = ejercicio.pk
        programa.save()
        planificacion = Planification.objects.create(**diccionario_planificacion)
        planificacion.programm_set = programa.pk
        return planificacion

    def test_planification_creation(self):
        p = self.create_planification()
        self.assertTrue(isinstance(p, Planification))
        self.assertEqual(p.__unicode__(), p.name)
