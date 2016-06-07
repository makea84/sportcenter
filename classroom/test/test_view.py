import unittest
from django.test import LiveServerTestCase
#from django.test import TestCase
from django.contrib.auth.models import User
from classroom.models import Classroom, Course, Participation, Place
from selenium import webdriver
#from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys
#from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from StringIO import StringIO

TEST_IMAGE = '''
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
'''.strip().decode('base64')



image = InMemoryUploadedFile(
            StringIO(TEST_IMAGE),
            field_name='image',
            name='1.JPG',
            content_type='image/jpg',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )

desktopFile = os.path.expanduser("~/Escritorio/1.JPG")
imagen = 'classroom/1.JPG'
#file = open(desktopFile, 'rw')
diccionario_clase ={
    'name':'nombre','width':'100.00','length':'100.00','description':'descripcion',
    'avaible':'Si','capacity':'10','image':image
}

diccionario_curso ={
    'name':'nombre','day':'Lunes','hour':'17:00','description':'descripcion',
    'duration':'02:00','cost':'100.00',
}

clase = Classroom.objects.get_or_create(**diccionario_clase)

class TestClassroom(LiveServerTestCase):

    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        #clase = Classroom.objects.get_or_create(**diccionario_clase)
        clase = Classroom.objects.get(name='nombre')
        print clase
        usuario = User.objects.create_superuser(username='root',password='root',email='admin@example.com')
        #curso = Course.objects.get_or_create(**diccionario_curso)
        curso = Course.objects.get(name='nombre')
        print curso
        Participation.objects.get_or_create(user=usuario, course=curso)
        Place.objects.get_or_create(classroom=clase, course=curso)
        

        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(TestClassroom, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestClassroom, self).tearDown()
        
        
    def test_create_classroom(self):
        self.selenium.get("http://localhost:8080/sportcenter/")
        form=self.selenium.find_element_by_id("login-form")
        username = form.find_element_by_id("id_username")
        username.send_keys("root")
        password = form.find_element_by_id("id_password")
        password.send_keys("root")
        form.submit()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_id("clases").click()
        self.selenium.implicitly_wait(10)
        formulario = self.selenium.find_element_by_id("crear-clase-form")
        name = formulario.find_element_by_id("id_name")
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        name.send_keys("nombre1")
        description = formulario.find_element_by_id("id_description")
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        description.send_keys("descripcion")
        width = formulario.find_element_by_id("id_width")
        width.send_keys(Keys.CONTROL + "a")
        width.send_keys(Keys.DELETE)
        width.send_keys("100.00")
        length = formulario.find_element_by_id("id_length")
        length.send_keys(Keys.CONTROL + "a")
        length.send_keys(Keys.DELETE)
        length.send_keys("100.00")
        avaible = formulario.find_element_by_id("id_avaible")
        avaible.send_keys(Keys.CONTROL + "a")
        avaible.send_keys(Keys.DELETE)
        avaible.send_keys("Si")
        capacity = formulario.find_element_by_id("id_capacity")
        capacity.send_keys(Keys.CONTROL + "a")
        capacity.send_keys(Keys.DELETE)
        capacity.send_keys("10")
        formulario.find_element_by_id("id_image").send_keys(desktopFile)
        formulario.submit()
        clase1 = Classroom.objects.get(name='nombre1')
        clase = Classroom.objects.get(name='nombre')
        self.assertTrue(clase1.width,clase.width)
        
    def test_change_classroom(self):
        self.selenium.get("http://localhost:8080/sportcenter/")
        form=self.selenium.find_element_by_id("login-form")
        username = form.find_element_by_id("id_username")
        username.send_keys("root")
        password = form.find_element_by_id("id_password")
        password.send_keys("root")
        form.submit()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_id("clases").click()
        formularios = self.selenium.find_elements_by_class_name("formulario-modificar-clase")
        formularios[0].submit()
        self.selenium.implicitly_wait(10)
        formulario= self.selenium.find_element_by_id("modificar-clase-form")
        name = formulario.find_element_by_id("id_name")
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        name.send_keys("nombre")
        description = formulario.find_element_by_id("id_description")
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        description.send_keys("descripcion")
        width = formulario.find_element_by_id("id_width")
        width.send_keys(Keys.CONTROL + "a")
        width.send_keys(Keys.DELETE)
        width.send_keys("100.00")
        length = formulario.find_element_by_id("id_length")
        length.send_keys(Keys.CONTROL + "a")
        length.send_keys(Keys.DELETE)
        length.send_keys("100.00")
        avaible = formulario.find_element_by_id("id_avaible")
        avaible.send_keys(Keys.CONTROL + "a")
        avaible.send_keys(Keys.DELETE)
        avaible.send_keys("Si")
        capacity = formulario.find_element_by_id("id_capacity")
        capacity.send_keys(Keys.CONTROL + "a")
        capacity.send_keys(Keys.DELETE)
        capacity.send_keys("10")
        formulario.find_element_by_id("id_image").send_keys(desktopFile);
        formulario.submit()
        self.selenium.implicitly_wait(10)
        currentURL = self.selenium.current_url;
        self.assertEquals(currentURL,"http://localhost:8080/sportcenter/clases/todas_clases/")
        
    def test_create_course(self):
        self.selenium.get("http://localhost:8080/sportcenter/")
        form=self.selenium.find_element_by_id("login-form")
        form.find_element_by_id("id_username").send_keys("root")
        form.find_element_by_id("id_password").send_keys("root")
        form.submit()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_id("clases").click()
        self.selenium.implicitly_wait(10)
        formulario = self.selenium.find_element_by_id("crear-curso-form")
        name = formulario.find_element_by_id("id_name")
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        name.send_keys("nombre")
        description = formulario.find_element_by_id("id_description")
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        description.send_keys("descripcion")
        day = formulario.find_element_by_id("id_day")
        day.send_keys(Keys.CONTROL + "a")
        day.send_keys(Keys.DELETE)
        day.send_keys("Martes")
        hour = formulario.find_element_by_id("id_hour")
        hour.send_keys(Keys.CONTROL + "a")
        hour.send_keys(Keys.DELETE)
        hour.send_keys("10:00")
        duration = formulario.find_element_by_id("id_duration")
        duration.send_keys(Keys.CONTROL + "a")
        duration.send_keys(Keys.DELETE)
        duration.send_keys("01:00")
        cost = formulario.find_element_by_id("id_cost")
        cost.send_keys(Keys.CONTROL + "a")
        cost.send_keys(Keys.DELETE)
        cost.send_keys("100.00")
        formulario.submit()
        self.selenium.implicitly_wait(10)
        currentURL = self.selenium.current_url;
        self.assertEquals(currentURL,"http://localhost:8080/sportcenter/clases/todas_clases/")
        
        
class TestViewCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
def upload_file(desktopFile):
    path = '/var/www/pictures/%s' % id
    f = desktopFile
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return True
