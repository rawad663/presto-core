from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware

from .views import *
from .models import *


class RegistrationViewTests(TestCase):


    def setUp(self):
      # Every test needs access to the request factory.
    
        self.u1 = User.objects.create(username='User1', first_name='Alice', last_name='Smith', email='user1@foo.com', password='pass', is_resto=True)
        self.u1.save()
        self.u2 = User.objects.create_user(username='User2', first_name='Bob', last_name='Frank', email='user2@foo.com', password='pass', is_resto=False)
        self.u2.save()
        self.u3 = Resto.objects.create(user=self.u1, created='2017-03-03', resto_name = "Alice's dinner", description='great food', phone_number="12345678", postal_code="H1H2H3")
        self.u3.save()
        self.u4 = Customer.objects.create(user=self.u2, liked_restos='')

    def test_registration_resto_view(self):
         url = reverse('register_resto')
         form_data= {
            'resto_name': "Alice's dinner",
            'description': 'great food',
            'phone_number': "12345678",
            'postal_code': "H1H2H3",
            'username': 'User1',
            'email': 'user1@foo.com',
            'first_name': 'Alice',
            'last_name': 'Smith', }
request = RequestFactory().post(url, data=form_data)

SessionMiddleware().process_request(request)
MessageMiddleware().process_request(request)
view = RegisterResto.as_view()
response=view(request)

self.failUnlessEqual(response.status_code, status.HTTP_201_CREATED)
self.assertEqual(Resto.objects.count(), 0)  


def test_register_customer_view(self):
        url= reverse('register_customer')
        form_data= {
            'username': 'User2',
            'email': 'user2@foo.com',
            'first_name': 'Bob',
            'last_name': 'Frank',
        }
request = RequestFactory().post(url, data=form_data)

SessionMiddleware().process_request(request)
MessageMiddleware().process_request(request)
view = RegisterCustomer.as_view()
response=view(request)

self.failUnlessEqual(response.status_code, status.HTTP_201_CREATED)
self.assertEqual(Customer.objects.count(), 0)  



        