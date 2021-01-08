from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *

#Client classes
class ClientRetrieveView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateView(generics.UpdateAPIView):
     queryset = Client.objects.all()
     serializer_class = CreateClientSerializer

class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#Realtor classes
class RealtorRetrieveView(generics.RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

class RealtorUpdateView(generics.UpdateAPIView):
     queryset = Realtor.objects.all()
     serializer_class = CreateRealtorSerializer

class RealtorCreateView(generics.CreateAPIView):
    queryset = Realtor.objects.all()
    serializer_class = CreateRealtorSerializer

class RealtorListView(generics.ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

#Offer classes
class OfferRetrieveView(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferUpdateView(generics.UpdateAPIView):
     queryset = Offer.objects.all()
     serializer_class = CreateOfferSerializer

class OfferCreateView(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = CreateOfferSerializer

class OfferListView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

#Requirement classes
class RequirementRetrieveView(generics.RetrieveAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

class RequirementUpdateView(generics.UpdateAPIView):
     queryset = Requirement.objects.all()
     serializer_class = RequirementSerializer

class RequirementCreateView(generics.CreateAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

class RequirementListView(generics.ListAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

#Deal classes
class DealRetrieveView(generics.RetrieveAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class DealUpdateView(generics.UpdateAPIView):
     queryset = Deal.objects.all()
     serializer_class = DealSerializer

class DealCreateView(generics.CreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class DealListView(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer