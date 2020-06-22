from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        # fields = '__all__'
        fields = ['id', 'username', 'birthday']


class UsersDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'birthday', 'is_superuser', 'is_staff']
