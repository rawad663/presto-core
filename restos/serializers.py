from restos.models import Resto
from rest_framework import serializers
from django.contrib.auth.models import User


class RestoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Resto
        fields = ('owner', 'id', 'created', 'name', 'description', 'picture')


class UserSerializer(serializers.ModelSerializer):
    restos = serializers.PrimaryKeyRelatedField(many=True, queryset=Resto.objects.all()) # why this? Restos is not an attribute of User

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'restos')

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['firstName'],
            last_name=validated_data['lastName']
        )
        user.set_password(validated_data['password'])
        user.save()

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'username', 'password')
