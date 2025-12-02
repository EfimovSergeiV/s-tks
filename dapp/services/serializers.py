from rest_framework import serializers
from services.models import *
from main.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesModel
        fields = ['id', 'name']


class SignatureSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)