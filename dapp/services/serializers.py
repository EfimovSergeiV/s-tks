from rest_framework import serializers
from .models import *


class SignatureSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    job = serializers.CharField(max_length=100)
    worker = serializers.CharField(max_length=20)
    private = serializers.CharField(max_length=20)
    whatsapp = serializers.CharField(max_length=20, allow_blank=True, required=False)
    telegramm = serializers.CharField(max_length=20, allow_blank=True, required=False)