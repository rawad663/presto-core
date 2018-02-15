# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from restos.models import Resto
from django.shortcuts import render
from restos.serializers import RestoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class RestoList(APIView):
    """
    List all restos, or create a new snippet.
    """
    def get(self, request, format=None):
        restos = Resto.objects.all()
        serializer = RestoSerializer(restos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This is the detail page
class RestoDetail(APIView):
    """
    Retrieve, update or delete a resto instance.
    """

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