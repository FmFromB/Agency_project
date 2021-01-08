from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User;
        fields = ['first_name', 'last_name', 'middle_name', 'phone', 'Email']