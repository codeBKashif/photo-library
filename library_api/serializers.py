from dataclasses import fields
from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("__all__")
    name = serializers.CharField()
    formats = serializers.CharField()
    destinations = serializers.CharField()
    file: serializers.CharField()
        