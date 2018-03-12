from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse

from .views import *
from .models import *


class RegistrationViewTests(APITestCase):


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

        resto = Resto.objects.get(pk=1)
        self.assertEqual(resto.resto_name, "Alice's dinner")
        self.assertEqual(Resto.objects.all().count(), 1)


class RestoListViewTest(APITestCase):

    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()


    def test_empty_restolist(self):

        url = reverse('resto_list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 0)    

    def test_restolist_view(self):
  
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

        response_bis = self.client.post(reverse('register_resto'), 
        data= {
            "resto_name": "Bob's pizza",
            "description": "pizza&pasta",
            "phone_number": "12345678",
            "postal_code": "H1H2H3",
            "user": {
            "username": "User2",
            "email": "user2@foo.com",
            "first_name": "Bob",
            "last_name": "Frank",
            "password":"pass"}},
        format='json'
        )

        resto = Resto.objects.get(pk=1)
        resto_bis = Resto.objects.get(pk=2)








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
