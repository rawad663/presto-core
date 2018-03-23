# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_resto = models.BooleanField('resto status', default=False)


class Resto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    resto_name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    phone_number = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    photo = models.FileField(default=None)

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
