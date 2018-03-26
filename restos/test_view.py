from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from .image_base64 import base_64_text
import json
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

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
            "address":"123 rue du fort",
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
            "address":"456 rue du fort",
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
            "photo": base_64_text.get_base64(),
            "address":"123 rue du fort",
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
            "photo": base_64_text.get_base64(),
            "address":"123 rue du fort",
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
            "photo": base_64_text.get_base64(),
            "address":"456 rue du fort",
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


class RestoLikeDislikeTest(APITestCase):
    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()

    def test_likeresto(self):
        response_resto = self.client.post(reverse('register_resto'),
        data= {
        "resto_name": "Alice's dinner",
        "description": "great food",
        "phone_number": "12345678",
        "postal_code": "H1H2H3",
        "address":"123 rue du fort",
        "user": {
        "username": "User1",
        "email": "user1@foo.com",
        "first_name": "Alice",
        "last_name": "Smith",
        "password":"pass"}},
        format='json'
        )

        response_restobis = self.client.post(reverse('register_resto'),
        data= {
        "resto_name": "Bob's pizza",
        "description": "pizza&pasta",
        "phone_number": "12345678",
        "postal_code": "H1H2H3",
        "address":"456 rue du fort",
        "user": {
        "username": "User2",
        "email": "user2@foo.com",
        "first_name": "Bob",
        "last_name": "Frank",
        "password":"pass"}},
        format='json'
        )

        url= reverse('register_customer')
        form_data= {
        "user": {
        "username": "User4",
        "email": "user4@foo.com",
        "first_name": "Bob",
        "last_name": "Frank",
        "password": "pass"
        }
        }
        response_cust = self.client.post(url, data=form_data, format='json')


        user = User.objects.get(pk=3)
        cust = Customer.objects.get(pk=3)
        resto = Resto.objects.get(pk=1)
        resto_bis = Resto.objects.get(pk=2)
        factory = APIRequestFactory()
        view = LikeResto.as_view()
        view_dis = DislikeResto.as_view()
        request = factory.post('/like-resto/', json.dumps({}), content_type='application/json')
        request_dis = factory.post('/dislike-resto/', json.dumps({}), content_type='application/json')
        force_authenticate(request, user=user)
        force_authenticate(request_dis, user=user)
        response = view(request, pk= resto.user.id)
        response_bis = view_dis(request_dis, pk = resto_bis.user.id)
        self.assertEqual(1, len(cust.liked_restos.all()))
        self.assertEqual(1, len(cust.disliked_restos.all()))


class MakeReservationTest(APITestCase):

    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()

    def test_make_reservation(self):
        response_resto = self.client.post(reverse('register_resto'),
        data= {
        "resto_name": "Alice's dinner",
        "description": "great food",
        "phone_number": "12345678",
        "postal_code": "H1H2H3",
        "address":"123 rue du fort",
        "user": {
        "username": "User1",
        "email": "user1@foo.com",
        "first_name": "Alice",
        "last_name": "Smith",
        "password":"pass"}},
        format='json'
        )


        url= reverse('register_customer')
        form_data= {
        "user": {
        "username": "User4",
        "email": "user4@foo.com",
        "first_name": "Bob",
        "last_name": "Frank",
        "password": "pass"
        }
        }
        response_cust = self.client.post(url, data=form_data, format='json')

    
        user = User.objects.get(pk=2)
        cust = Customer.objects.get(pk=2)
        resto = Resto.objects.get(pk=1)
        factory = APIRequestFactory()
        view = MakeReservation.as_view()
        view_bis = Reservations.as_view()
        request = factory.post('/reserve/', data={
        "customer": "user4",
        "resto": "Alice's dinner",
        "datetime": "2018-03-27 19:30", 
        "num_people": "3",
        "status":"p"}, format='json')
        request_bis = factory.get('/reservations/', content_type='application/json')
        force_authenticate(request, user=user)
        force_authenticate(request_bis, user=user)
        response = view(request, customerPk=cust.user.id, restoPk=resto.user.id)
        response_bis = view_bis(request_bis)
        self.assertEqual(1, Reservation.objects.all().count())


class CustomerProfileTest(APITestCase):
    
    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()

    def test_viewprofile(self):
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
        user = User.objects.get(pk=1)
        cust = Customer.objects.get(pk=1)
        factory = APIRequestFactory()
        view = CustomerDetail.as_view()
        request = factory.get('/customers/', content_type='application/json')
        force_authenticate(request, user=user)
        response = view(request, pk= cust.user.id)
        self.assertEqual("User2", cust.user.username)


class RestoEditTest(APITestCase):

    def tearDown(self):    
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()

    def test_editprofile(self):
        request = self.client.post(reverse('register_resto'), 
        data= {
            "resto_name": "Alice's dinner",
            "description": "great food",
            "phone_number": "12345678",
            "postal_code": "H1H2H3",
            "photo": base_64_text.get_base64(),
            "address":"123 rue du fort",
            "user": {
            "username": "User1",
            "email": "user1@foo.com",
            "first_name": "Alice",
            "last_name": "Smith",
            "password":"pass"}},
        format='json'
        )
        user = User.objects.get(pk=1)
        resto = Resto.objects.get(pk=1)
        factory = APIRequestFactory()

        self.assertEqual("Alice's dinner", resto.resto_name) 

        request_bis = factory.patch('/customers/', data= {"resto_name":"Plaza"}, format='json') 
        view = RestoDetail.as_view()
        response = view(request_bis, pk=resto.user.id)
        restobis = Resto.objects.get(pk=1)
        print(response.data)
        self.assertEqual("Plaza", restobis.resto_name) 



'''
class ReservationViewTest(APITestCase):
    def tearDown(self):
        User.objects.all().delete()
        Resto.objects.all().delete()
        Customer.objects.all().delete()

    def test_accept_reservation_resto_view(self):

    def test_reservation_customer_view(self):

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


test for Login, should work for both customer and resto
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
