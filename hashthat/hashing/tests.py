from django.test import TestCase
from selenium import webdriver
from django.test import Client
c = Client()
from .forms import HashForm
import hashlib
from .models import Hash
from django.core.exceptions import ValidationError
import time

class FunctionTestCase(TestCase):
    def setUp(self):
        self.brouser = webdriver.Firefox()

    def test_home_page(self):
        self.brouser.get('http://localhost:8000')
        self.assertIn("Enter hash here", self.brouser.page_source)

    def test_hash_of_hello(self):
        self.brouser.get('http://localhost:8000')
        text = self.brouser.find_element_by_id("id_text")
        text.send_keys("hello")
        self.brouser.find_element_by_name("submit").click()
        self.assertIn("2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824", self.brouser.page_source)


    def test_hash_ajax(self):    
        self.brouser.get('http://localhost:8000')
        text = self.brouser.find_element_by_id("id_text")
        text.send_keys("hello")
        time.sleep(5) #wait for 5sec
        self.assertIn(
            '2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.brouser.page_source)

    def tearDown(self):
        self.brouser.quit()


class UnitTestCase(TestCase):
    def test_home_homepage_template(self):
        response = c.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        form = HashForm(data = {'text':'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertNotEqual('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', text_hash)    

    def saveHash(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824'
        hash.save()
        return hash

    def test_hash_object(self):
        hash = self.saveHash()
        pulled_hash = Hash.objects.get(
            hash='2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824')
        self.assertNotEqual(hash.text, pulled_hash)  

    

    def test_viewing_hash(self):
        hash = self.saveHash()
        response = c.get(
            '/hash/2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824')
        self.assertContains(response, 'hello')


    def test_bad_data(self):
        def badHash():
            hash = Hash()
            hash.hash = "geggg"
            hash.full_clean()
            self.assertRaises(ValidationError, badHash)


