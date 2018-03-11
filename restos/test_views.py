from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

from .views import Register, RestoList


class RegistrationViewTests(RegistrationTestCase):

    def test_registration_view(self):
    
    
        response = self.client.post(reverse('Register'),
                                    data={ 'username': 'alice123', 
                                           'email': 'foo@example.com',
                                           'password': 'foo',
                                           'first_name': 'alice',
                                           'last_name': 'smith'})
        self.assertEqual(response.status_code, 200)
    

       response = self.client.post(reverse('Register'),
                                    data={ 'username': 'alice123', 
                                           'email': 'foo@example.com',
                                           'password': 'foo',
                                           'first_name': 'alice',
                                           'last_name': 'smith'})
        self.assertEqual(response.status_code, 302)


    def test_restolist_view(self):

        