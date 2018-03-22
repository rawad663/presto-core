# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_resto = models.BooleanField('resto status', default=False)

class Resto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    resto_name = models.CharField(max_length=100, default='') # remove blank
    description = models.TextField(default='')
    phone_number = models.CharField(max_length=20, default='')
    postal_code = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=30, default='')

    class Meta:
        ordering = ('created',)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    liked_restos = models.ManyToManyField(Resto, blank=True, related_name='liked_restos')
    disliked_restos = models.ManyToManyField(Resto, blank=True, related_name='disliked_restos')

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    resto = models.ForeignKey(Resto, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)

    STATUSCHOICE = (
        ('a', 'Accepted'),
        ('d', 'Declined'),
        ('p', 'Pending'),
    )
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default='p')
