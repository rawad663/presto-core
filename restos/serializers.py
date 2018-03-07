from restos.models import Resto, User
from rest_framework import serializers
#from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            isResto=False
        )
        user.set_password(validated_data['password'])
        #user.save()
        

        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'isResto')

class RestoSerializer(serializers.ModelSerializer):
    user = CustomerSerializer(required=True)
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomerSerializer.create(CustomerSerializer(), validated_data=user_data)
        user.isResto = True

        return Resto.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            user=user
        )

    class Meta:
        model = Resto
        fields = ('user', 'name', 'description')