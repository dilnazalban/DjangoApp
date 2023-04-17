from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import App


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'last_name', 'first_name']


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["name", 'category', "description", "size", "poster", "created_at", "installers"]
