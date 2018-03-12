from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware

from .views import *
from .models import *


class RegistrationViewTests(APITestCase):


    def setUp(self):
  
        self.u1 = User.objects.create(username='User1', first_name='Alice', last_name='Smith', email='user1@foo.com', password='pass', is_resto=True)
        self.u1.save()
        self.u2 = User.objects.create(username='User2', first_name='Bob', last_name='Frank', email='user2@foo.com', password='pass', is_resto=False)
        self.u2.save()
        self.u3 = User.objects.create(username='User3', first_name='Liz', last_name='Abo', email='user3@foo.com', password='pass', is_resto=False)
        self.u3.save()
        self.u4 = Resto.objects.create(user=self.u1, created='2017-03-03', resto_name = "Alice's dinner", description='great food', phone_number="12345678", postal_code="H1H2H3")
        self.u4.save()
        self.u5 = Customer.objects.create(user=self.u2)
        self.u6 = Customer.objects.create(user=self.u3)

    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()


    def test_register_customer_view(self):
        url= reverse('register_customer')
        form_data= {
        "user": {
        "username": "User2",
        "email": "user2@foo.com",
        "first_name": "Bob",
        "last_name": "Frank",
        "password": "pass"
            }
        }
        response = self.client.post(url, data=form_data, format='json')

        url= reverse('register_customer')
        form_data= {
        "user": {
        "username": "User3",
        "email": "user3@foo.com",
        "first_name": "Bobd",
        "last_name": "Frank",
        "password": "pass"
            }
        }
        response1 = self.client.post(url, data=form_data, format='json')

        self.assertEqual(Customer.objects.all().count(), 2)  


    def test_registration_resto_view(self):
        response = self.client.post(reverse('register_resto'), 
        data= {
            "resto_name": "Alice's dinner",
            "description": "great food",
            "phone_number": "12345678",
            "postal_code": "H1H2H3",
            "user": {
            "username": "User1",
            "email": "user1@foo.com",
            "first_name": "Alice",
            "last_name": "Smith",
            "password":"pass"}},
        format='json'
        )


        
        self.assertEqual(Resto.objects.all().count(), 1)  







'''
test for Login, should work for both customer and resto
    need to have login implemented first 
    class LoginViewTests(TestCase)
        def setUp(self):
            self.credentials = {
                'username': 'testcustomer',
                'password': 'verysecurepassword'
            }
            User.objects.create_user(**self.credentials)

        def test_login(self):
            response = self.client.post('/login', self.credentials, follow=True)
            self.assertTrue(response.context['user'].is_authenticated)
'''
