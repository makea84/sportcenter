
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver



class AdminTestCase(LiveServerTestCase):
    
    def setUp(self):
        User.objects.create_superuser(
            username='root',
            password='root',
            email='admin@example.com'
        )
        if(User.objects.all().filter(username='usuario').exists()):
            User.objects.get(username='usuario').delete()
            
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AdminTestCase, self).tearDown()

    def test_create_user(self):
        self.selenium.get("http://localhost:8080/sportcenter/")
        form=self.selenium.find_element_by_id("register-form")
        name = form.find_element_by_id("id_name")
        name.send_keys("usuario")
        dni = form.find_element_by_id("id_dni")
        dni.send_keys("11111111-A")
        username = form.find_element_by_id("id_username")
        username.send_keys("usuario")
        password = form.find_element_by_id("id_password")
        password.send_keys("usuario")
        email = form.find_element_by_id("id_email")
        email.send_keys("usuario@gmail.com")
        form.submit()
        self.selenium.implicitly_wait(10)
        currentURL = self.selenium.current_url;
        self.assertEquals(currentURL,"http://localhost:8080/sportcenter/")

    def test_login_user(self):
        self.selenium.get("http://localhost:8080/sportcenter/")
        form=self.selenium.find_element_by_id("login-form")
        username = form.find_element_by_id("id_username")
        username.send_keys("root")
        password = form.find_element_by_id("id_password")
        password.send_keys("root")
        form.submit()
        self.selenium.implicitly_wait(10)
        currentURL = self.selenium.current_url;
        self.assertEquals(currentURL,"http://localhost:8080/sportcenter/home/")