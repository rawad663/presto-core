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

    def test_emptycustomermodel(self):

        self.assertEqual(Customer.objects.all().count(), 0)
    
    
    def test_emptyrestomodel(self):

        self.assertEqual(Resto.objects.all().count(), 0)


    def test_invalidpostalcode(self):
        
        response = self.client.post(reverse('register_resto'), 
        data= {
            "resto_name": "Alice's dinner",
            "description": "great food",
            "phone_number": "12345678",
            "postal_code": "H1H2H3H1H2H3H1H2H3H1H2",
            "user": {
            "username": "User1",
            "email": "user1@foo.com",
            "first_name": "Alice",
            "last_name": "Smith",
            "password":"pass"}},
        format='json'
        )

        self.assertEqual(Resto.objects.all().count(), 0)
        self.assertIsNot(response, Resto) 

    
    def test_invalidphonenumber(self):
        
        response = self.client.post(reverse('register_resto'), 
        data= {
            "resto_name": "Alice's dinner",
            "description": "great food",
            "phone_number": "1234567891234567890012",
            "postal_code": "H1H2H3",
            "user": {
            "username": "User1",
            "email": "user1@foo.com",
            "first_name": "Alice",
            "last_name": "Smith",
            "password":"pass"}},
        format='json'
        )

        self.assertEqual(Resto.objects.all().count(), 0)    
        self.assertIsNot(response, Resto)       


        


    def test_registercustomerview(self):
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
        "first_name": "Leo",
        "last_name": "Abraham",
        "password": "pass"
            }
        }
        response1 = self.client.post(url, data=form_data, format='json')


        self.assertEqual(Customer.objects.all().count(), 2)  


    def test_registrationrestoview(self):
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
        self.assertEqual(resto.description, "great food")
        self.assertEqual(Resto.objects.all().count(), 1)



class RestoListViewTest(APITestCase):

    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()


    def test_emptyrestolist(self):

        url = reverse('resto_list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 0)    

    def test_restolistview(self):
  
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
        
        url = reverse('resto_list')
        response = self.client.get(url, format='json')

        self.assertEqual(len(response.data), 2) 



class ReservationViewTest(APITestCase):
    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()
    
    def test_reservation_customer_view(self):
    def test_accept_reservation_resto_view(self):
    def test_cancel_reservation_customer_view(self):
    def test_decline_reservation_resto_view(self):


class EditCustomerViewTest(APITestCase):
    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()

    def test_edit_first_name_customer_view(self):
    def test_edit_last_name_customer_view(self):
    def test_edit_image_customer_view(self):
 

class LoginViewTest(APITestCase):
    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()
    
    def test_login_customer_view(self):
    def test_login_resto_view(self):


'''test for Login, should work for both customer and resto
    need to have login implemented first
class LoginViewTests(APITestCase):
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
