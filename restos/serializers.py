from restos.models import Resto
from rest_framework import serializers
from django.contrib.auth.models import User


class RestoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Resto
        fields = ('owner', 'id', 'created', 'name', 'description', 'picture')


class UserSerializer(serializers.ModelSerializer):
    restos = serializers.PrimaryKeyRelatedField(many=True, queryset=Resto.objects.all())

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'snippets')
