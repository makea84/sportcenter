from django.test import TestCase
from machine.models import Machine, Exercise, Programm
from machine.forms import MachineForm, ExerciseForm, ProgrammForm, PlanificationForm
from django.core.files.uploadedfile import InMemoryUploadedFile
from StringIO import StringIO

TEST_IMAGE = '''
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
'''.strip().decode('base64')


diccionario_maquina ={'name':'nombre','description':'descripcion','image':'imagen','quantity':'01'}
diccionario_ejercicio ={'name':'nombre','image':'imagen','zone':'Brazos'}
diccionario_programa ={'name':'nombre','quantity':'10','series':'10','rest':'10'}
diccionario_planificacion ={'name':'nombre','day':'Lunes'}
    
class MachineTest(TestCase):
    
    def test_valid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'nombre','description':'descripcion','quantity':'10'}
        form = MachineForm(data=data, files={'image':image})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'','description':'descripcion','quantity':'10'}
        form = MachineForm(data=data, files={'image':image})
        self.assertFalse(form.is_valid())

        
class ExerciseTest(TestCase):

    def test_valid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'nombre','description':'descripcion','quantity':'10','image':image.name}
        maquina = Machine.objects.create(**data)
        data ={'name':'nombre','zone':'Brazos','machine':maquina.pk}
        form = ExerciseForm(data=data, files={'image':image})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'nombre','description':'descripcion','quantity':'10','image':image.name}
        maquina = Machine.objects.create(**data)
        data ={'name':'','zone':'Brazos','machine':maquina.pk}
        form = ExerciseForm(data=data, files={'image':image})
        self.assertFalse(form.is_valid())

class ProgrammTest(TestCase):

    def test_valid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'nombre','description':'descripcion','quantity':'10','image':image.name}
        maquina = Machine.objects.create(**data)
        data ={'name':'nombre','zone':'Brazos','machine':maquina}
        data2 ={'name':'nombre2','zone':'Brazos','machine':maquina}
        ejercicio = Exercise.objects.create(**data)
        ejercicio2 = Exercise.objects.create(**data2)
        Lista = [ejercicio.pk, ejercicio2.pk]
        data={'name':'nombre','quantity':'10','series':'10','rest':'10','exercise':Lista}
        form = ProgrammForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'nombre','description':'descripcion','quantity':'10','image':image.name}
        maquina = Machine.objects.create(**data)
        data ={'name':'nombre','zone':'Brazos','machine':maquina}
        data2 ={'name':'nombre2','zone':'Brazos','machine':maquina}
        ejercicio = Exercise.objects.create(**data)
        ejercicio2 = Exercise.objects.create(**data2)
        Lista = [ejercicio.pk, ejercicio2.pk]
        data={'name':'','quantity':'10','series':'10','rest':'10','exercise':Lista}
        form = ProgrammForm(data=data)
        self.assertFalse(form.is_valid())

        
class PlanificationTest(TestCase):

    def test_valid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'nombre','description':'descripcion','quantity':'10','image':image.name}
        maquina = Machine.objects.create(**data)
        data ={'name':'nombre','zone':'Brazos','machine':maquina}
        data2 ={'name':'nombre2','zone':'Brazos','machine':maquina}
        ejercicio = Exercise.objects.create(**data)
        ejercicio2 = Exercise.objects.create(**data2)
        Lista = [ejercicio.pk, ejercicio2.pk]
        data={'name':'nombre','quantity':'10','series':'10','rest':'10'}
        data2={'name':'nombre2','quantity':'10','series':'10','rest':'10'}
        programa = Programm.objects.create(**data)
        programa.exercise_set = Lista
        programa.save()
        programa2 = Programm.objects.create(**data2)
        programa2.exercise_set = Lista
        programa2.save()
        Lista = [programa.pk, programa2.pk]
        data ={'name':'nombre','day':'Lunes','programm':Lista}
        form = PlanificationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        data ={'name':'nombre','description':'descripcion','quantity':'10','image':image.name}
        maquina = Machine.objects.create(**data)
        data ={'name':'nombre','zone':'Brazos','machine':maquina}
        data2 ={'name':'nombre2','zone':'Brazos','machine':maquina}
        ejercicio = Exercise.objects.create(**data)
        ejercicio2 = Exercise.objects.create(**data2)
        Lista = [ejercicio.pk, ejercicio2.pk]
        data={'name':'nombre','quantity':'10','series':'10','rest':'10'}
        data2={'name':'nombre2','quantity':'10','series':'10','rest':'10'}
        programa = Programm.objects.create(**data)
        programa.exercise_set = Lista
        programa.save()
        programa2 = Programm.objects.create(**data2)
        programa2.exercise_set = Lista
        programa2.save()
        Lista = [programa.pk, programa2.pk]
        data ={'name':'','day':'Lunes','programm':Lista}
        form = PlanificationForm(data=data)
        self.assertFalse(form.is_valid())
