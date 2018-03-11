from restos.models import Resto, User, Reservation, Customer
from rest_framework import serializers
#from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_resto=False
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_resto')

class RestoSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_resto = True
        user.save()

        return Resto.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            user=user
        )

    #def update()

    class Meta:
        model = Resto
        fields = ('user', 'resto_name', 'description')

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    liked_restos = RestoSerializer(required=False, many=True)
    # vivek
    disliked_restos = RestoSerializer(required=False, many=True)

    class Meta:
        model = Customer
        fields = ('user', 'liked_restos', 'disliked_restos')

class CustomerSimpleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_resto = False
        user.save()

        return Customer.objects.create(user=user)

    class Meta:
        model = Customer
        fields = ('user',)

class ReservationSerializer(serializers.ModelSerializer):
    customer = CustomerSimpleSerializer(required=True)
    resto = RestoSerializer(required=True)
    
    def create(self, validated_data, customer, resto):
        return Reservation.objects.create(
            customer=customer,
            resto=resto,
            datetime=validated_data["datetime"]
        )

    #def update()

    class Meta:
        model = Reservation
        fields = ('customer', 'resto', 'datetime')