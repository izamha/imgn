from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (Umugani, )
from users.models import CustomUser

""" For user || groups and their permissions, not so important now"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


""" The real stuff """


class UmuganiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umugani
        fields = '__all__'


class UmuganiCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umugani
        fields = ('title', 'meaning', 'application', 'caricature',)
