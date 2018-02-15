from restos.models import Resto
from rest_framework import serializers


class RestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resto
        fields = ('id', 'created', 'name', 'description', 'picture')