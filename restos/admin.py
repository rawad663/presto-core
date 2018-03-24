# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Resto, User, Customer, Reservation
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin

# Register your Resto here.
admin.site.register(User)
admin.site.register(Resto)
admin.site.register(Customer)
admin.site.register(Reservation)
