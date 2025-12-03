from rest_framework import serializers
from services.models import *
from main.models import *


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователей (all)"""
    
    class Meta:
        model = EmployeesModel
        fields = "__all__"


class BannerImageSerializer(serializers.ModelSerializer):
    """ Сериализатор баннеров к подписи ('link', 'image') """

    class Meta:
        model = BannerImageModel
        fields = ['link', 'image']


class CatalogsSerializer(serializers.ModelSerializer):
    """ Cериализатор каталогов (__all__) """

    class Meta:
        model = CatalogModel
        fields = "__all__"


class SignatureSerializer(serializers.Serializer):
    """ Cериализатор подписи email (id, name, logo, banner_images, catalogs) """

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    logo = serializers.ImageField()
    banner_images = BannerImageSerializer(many=True)
    catalogs = CatalogsSerializer(many=True)