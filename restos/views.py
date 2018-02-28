# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from restos.models import Resto
from rest_framework import permissions, status, generics
from restos.serializers import RestoSerializer, UserSerializer, RegistrationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from restos.permissions import IsOwnerOrReadOnly, IsSelfOrReadOnly
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("TESTING TO PUSH FROM MULTIPLE COLLABORATORS")

class RestoList(APIView):
    def get(self, request):
        queryset = Resto.objects.all()
        serializer_class = RestoSerializer(queryset, many = True)
        return Response(serializer_class.data)


# This is the detail page
class RestoDetail(APIView):
    """
    Retrieve, update or delete a resto instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,) # SHOULD THIS NOT JUST BE IS OWNERORREADONLY? If you put authenticated too,
    # then anyone who's authenticated might create or update a rest
    def get_object(self, pk):
        try:
            return Resto.objects.get(pk=pk)
        except Resto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        resto = self.get_object(pk)
        serializer = RestoSerializer(resto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        resto = self.get_object(pk)
        serializer = RestoSerializer(resto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        resto = self.get_object(pk)
        resto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" 
This is the user detail page.
Users browse other users but user can only edit their own page.
There are permissions and cRUD actions available.
"""


class UserDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSelfOrReadOnly)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except Resto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Register(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        # Creating new User
        if serializer.is_valid():
            User.objects.create_user(
                serializer.initial_data['email'],
                serializer.initial_data['username'],
                serializer.initial_data['password']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # username = request.POST.get('username')
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # first_name = request.POST.get('firstName')
        # last_name = request.POST.get('lastName')
        #
        # user = User.objects.create_user(username, email, password)
        # user.first_name = first_name
        # user.last_name = last_name
        # user.save()
        #
        # # Generating token for user
        # token = Token.objects.create(user=user)
        #
        # return Response({'detail': 'User has been created successfully', 'Token': token.key})


class ChangePassword(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user)
        user.set_password(request.POST.get('new_password'))
        user.save()

        return Response({'detail': 'Password has been updated'})