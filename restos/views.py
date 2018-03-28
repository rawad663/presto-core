# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from restos.models import Resto, User, Customer, Reservation
from rest_framework import permissions, status, generics
from restos.serializers import RestoSerializer, CustomerSerializer, ReservationSerializer, UserSerializer, CustomerSimpleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from restos.permissions import IsOwnerOrReadOnly, IsSelfOrReadOnly
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import CreateView
from rest_framework.authtoken.views import ObtainAuthToken
# from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("TESTING TO PUSH FROM MULTIPLE COLLABORATORS")

class RestoList(APIView):
    #permissions

    def get(self, request):
        restos = Resto.objects.all()
        serializer = RestoSerializer(restos, many=True)
        return Response(serializer.data)

class CustomerList(APIView):
    #permissions

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(pk=token.user_id)
        if user.is_resto:
            resto = Resto.objects.get(pk=token.user_id)
            serializer = RestoSerializer(resto)
            return Response({'token': token.key, 'resto': serializer.data})
        else:
            customer = Customer.objects.get(pk=token.user_id)
            serializer = CustomerSimpleSerializer(customer)
            return Response({'token': token.key, 'customer': serializer.data})


# This is the detail page
class RestoDetail(APIView):
    """
    Retrieve, update or delete a resto instance.
    """
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, pk, format=None):
        resto = get_object_or_404(Resto, pk=pk)
        serializer = RestoSerializer(resto)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        resto = get_object_or_404(Resto, pk=pk)
        serializer = RestoSerializer(resto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     resto = self.get_object(pk)
    #     resto.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerDetail(APIView):
    """
    Retrieve, update or delete a customer instance.
    """
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, pk, format=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    # def delete(self, request, pk, format=None):
    #     customer = self.get_object(pk)
    #     customer.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterCustomer(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomerSimpleSerializer

    def post(self, request, *args, **kwargs):
        serializer = CustomerSimpleSerializer(data=request.data)
        # Creating new User
        if serializer.is_valid():
            token = Token.objects.create(user=serializer.save().user)
            return Response({"token": token.key, "customer": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        # # Generating token for user
        # token = Token.objects.create(user=user)
        #
        # return Response({'detail': 'User has been created successfully', 'Token': token.key})


class RegisterResto(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RestoSerializer

    def post(self, request, *args, **kwargs):
        serializer = RestoSerializer(data=request.data)
        # Creating new User
        if serializer.is_valid():
            token = Token.objects.create(user=serializer.save().user)
            return Response({"token": token.key, "resto": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # # Generating token for user
        # token = Token.objects.create(user=user)
        #
        # return Response({'detail': 'User has been created successfully', 'Token': token.key})

class LikeResto(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        user_resto = get_object_or_404(User, pk=pk)
        resto = None
        if user_resto.is_resto:
            resto = user_resto.resto
        else:
            return Response({"Message": "ID belongs to that of a customer. Only restos can be liked."}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if user.is_resto == True:
            return Response({"Message": "Resto cannot like another Resto"}, status=status.HTTP_400_BAD_REQUEST)
        
        customer = user.customer
        customer.liked_restos.add(resto)
        # if liked resto was a disliked resto, remove that resto from disliked resto list
        if resto in customer.disliked_restos.all():
            customer.disliked_restos.remove(resto)
        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DislikeResto(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        # get the disliked resto (if it isnt a 404 error)?
        user_resto = get_object_or_404(User, pk = pk)
        resto = None
        # if requested resto to be disliked is a resto
        if user_resto.is_resto:
            resto = user_resto.resto
        else:
            return Response({"Message": "ID belongs to that of a customer. Only restos can be disliked."}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if user.is_resto == True:
            return Response({"Message": "Resto cannot dislike another Resto"}, status=status.HTTP_400_BAD_REQUEST)
        
        customer = user.customer
        customer.disliked_restos.add(resto)
        # if disliked resto was a liked resto, remove that resto from liked resto list
        if resto in customer.liked_restos.all():
            customer.liked_restos.remove(resto)
        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MakeReservation(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, customerPk, restoPk):
        user_customer = get_object_or_404(User, pk=customerPk)
        user_resto = get_object_or_404(User, pk=restoPk)

        resto = None
        customer = None

        if not user_customer.is_resto:
            customer = user_customer.customer
        else:
            return Response({"Message": "Customer ID belongs to that of a resto"}, status=status.HTTP_400_BAD_REQUEST)
        if user_resto.is_resto:
            resto = user_resto.resto
        else:
            return Response({"Message": "Resto ID belongs to that of a customer"}, status=status.HTTP_400_BAD_REQUEST)

        reservation = ReservationSerializer.create(ReservationSerializer(), request.data, customer, resto)
        reservation.save()
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReserveDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        serializer = CustomerSerializer(resto)
        return Response(serializer.data)

    def delete(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        user = request.user
        if user == reservation.customer.user or user == reservation.resto.user:
            reservation.delete()
            return Response({"Message": "Reservation is deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"Message": "User cannot delete a reservation that is not his own"}, status=status.HTTP_400_BAD_REQUEST)



class Reservations(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        if user.is_resto:
            reservations = user.resto.reservation_set.all()
        else:
            reservations = user.customer.reservation_set.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class AcceptReservation(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        user = request.user
        if user != reservation.resto.user:
            return Response({"Message": "Resto cannot accept a reservation that is not attributed to him"}, status=status.HTTP_400_BAD_REQUEST)
        reservation.status = 'a'
        reservation.save()
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK) 

class DeclineReservation(APIView):
    def put(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        user = request.user
        if user != reservation.resto.user:
            return Response({"Message": "Resto cannot decline a reservation that is not attributed to it"}, status=status.HTTP_400_BAD_REQUEST)
        reservation.status = 'd'
        reservation.save()
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)

''' class ChangePassword(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user)
        user.set_password(request.POST.get('new_password'))
        user.save()

        return Response({'detail': 'Password has been updated'}) '''

