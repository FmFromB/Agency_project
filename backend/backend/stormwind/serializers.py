from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client;
        fields = '__all__'

class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client;
        fields = '__all__'

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor;
        fields = '__all__'

class CreateRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor;
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer;
        fields = '__all__'

class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer;
        fields = '__all__'

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement;
        fields = '__all__'

class CreateRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement;
        fields = '__all__'

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal;
        fields = '__all__'

class CreateDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal;
        fields = '__all__'




