from django.test import TestCase
from selenium import webdriver
from django.test import Client
from .forms import HashForm

# class FunctionTestCase(TestCase):
#     def setUp(self):
#         self.brouser = webdriver.Firefox()

#     def test_home_page(self):
#         self.brouser.get('http://localhost:8000')
#         self.assertIn("Enter hash here", self.brouser.page_source)

#     def test_hash_of_hello(self):
#         self.brouser.get('http://localhost:8000')
#         text = self.brouser.find_element_by_id("id_text")
#         text.send_keys("hello")
#         self.brouser.find_element_by_name("submit").click()
#         self.assertIn("2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824", self.brouser.page_source)


#     def tearDown(self):
#         self.brouser.quit()


class UnitTestCase(Client):
    def test_home_homepage_template(self):
        response = self.Client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        form = HashForm(data = {'text':'hello'})
        self.assertTrue(form.is_valid())
