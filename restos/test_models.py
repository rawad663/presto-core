# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from restos.models import Resto

from django.contrib.auth.models import User


# Create your tests here.

class RestoTestCase(TestCase):
    def setUp(self):
     self.u = User.objects.create(username='Bob')
     r = Resto.objects.Create(owner = self.u, created = '2017-03-03', name = "Bob's dinner", description = '', picture = '')
 
    def create_resto(self, owner = self.u, created = '2017-03-03', name = "Bob's dinner", description = '', picture = ''):
        return Resto.objects.create(owner=owner, created=created, name=name, description=description, picture=picture)

    def test_resto_creation(self):
        resto = self.create_resto()
    self.assertTrue(isinstance(resto, Resto))
    self.assertEqual(resto.name, r.name)


    def test_resto_count(self):
        self.assertEqual(Resto.objects.count(), 1)    

