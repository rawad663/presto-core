from restos.models import Resto, User, Reservation, Customer
from rest_framework import serializers
from django.core.files.base import ContentFile
from drf_extra_fields.fields import Base64ImageField
import image


# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_resto=False
        )
        user.set_password(validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_resto')


class RestoSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    photo = Base64ImageField()  # Image file from base64 here

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_resto = True

        resto_name = validated_data['resto_name']
        description = validated_data['description']
        phone_number = validated_data['phone_number']
        postal_code = validated_data['postal_code']
        address = validated_data['address']
        user.save()

        # Decode the photo data here
        photo = validated_data.pop('photo')

        resto = Resto(
            resto_name=resto_name,
            description=description,
            phone_number=phone_number,
            postal_code=postal_code,
            address=address,
            user=user,
            photo=photo
        )
        resto.save()
        return resto

    def update(self, instance, validated_data):
        # instance.user = validated_data.pop('user')
        instance.resto_name = validated_data.get('resto_name', instance.resto_name)
        instance.description = validated_data.get('description', instance.description)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.address = validated_data.get('address', instance.address)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance

    class Meta:
        model = Resto
        fields = ('user', 'resto_name', 'description', 'phone_number', 'postal_code', 'address', 'photo')


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    liked_restos = RestoSerializer(required=False, many=True)
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
        customer = Customer(
            user=user
        )
        customer.save()
        return customer

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
            datetime=validated_data["datetime"],
            status='p'
        )

    # def update()

    class Meta:
        model = Reservation
        fields = ('customer', 'resto', 'datetime', 'status')
