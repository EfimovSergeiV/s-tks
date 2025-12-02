from rest_framework import serializers
from services.models import *
from main.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesModel
        fields = ['id', 'name']


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImageModel
        fields = ['link', 'image']


class SignatureSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    logo = serializers.ImageField()
    banner_images = BannerImageSerializer(many=True)