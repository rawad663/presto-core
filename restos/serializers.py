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
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
