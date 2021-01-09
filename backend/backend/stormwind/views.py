from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *
#Logout class
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class IsRealtor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.Realtor == request.Realtor

#Client classes
class ClientRetrieveView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateView(generics.UpdateAPIView):
     queryset = Client.objects.all()
     serializer_class = CreateClientSerializer
     permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

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
     permissions_classes = (IsRealtor, )

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
     permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

class OfferCreateView(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = CreateOfferSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

class OfferListView(generics.ListAPIView):
    serializer_class = OfferSerializer

    def get_queryset(self):
        queryset = Offer.objects.all()
        params = self.request.query_params

        type_of_property = params.get('type_of_property', None)
        price = params.get('price', None)
        address = params.get('adress', None)
        floor = params.get('floor', None)
        rooms = params.get('rooms', None)
        area = params.get('area', None)
        floor_count = params.get('floor_count', None)

        if type_of_property:
            queryset = queryset.filter(type_of_property=type_of_property)

        if price:
            queryset = queryset.filter(price__lte=price)
        
        if floor:
            queryset = queryset.filter(floor__lte=floor)
        
        if rooms:
            queryset = queryset.filter(rooms__lte=rooms)

        if area:
            queryset = queryset.filter(area__lte=area)

        if floor_count:
            queryset = queryset.filter(floor_count__lte=floor_count)

        return queryset


#Requirement classes
class RequirementRetrieveView(generics.RetrieveAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

class RequirementUpdateView(generics.UpdateAPIView):
     queryset = Requirement.objects.all()
     serializer_class = RequirementSerializer
     permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

class RequirementCreateView(generics.CreateAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

class RequirementListView(generics.ListAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

    def get_queryset(self):
        queryset = Requirement.objects.all()
        params = self.request.query_params
     
        type_of_property = params.get('type_of_property', None)
        max_price = params.get('max_price', None)
        min_price = params.get('min_price', None)
        max_area = params.get('max_area', None)
        min_area = params.get('min_area', None)
        max_room_count = params.get('max_room_count', None)
        min_room_count = params.get('min_room_count', None)
        max_floor = params.get('max_floor', None)
        min_floor = params.get('min_floor', None)
        max_floor_count = params.get('max_floor_count', None)
        min_floor_count = params.get('min_floor_count', None)
     
        if type_of_property:
            queryset = queryset.filter(type_of_property=type_of_property)
     
        if max_price:
            queryset = queryset.filter(max_price__lte=max_price)
     
        if min_price:
            queryset = queryset.filter(min_price__gte=min_price)

        if max_area:
            queryset = queryset.filter(max_area__lte=max_area)
     
        if min_area:
            queryset = queryset.filter(min_area__gte=min_area)

        if max_room_count:
            queryset = queryset.filter(max_room_count__lte=max_room_count)
     
        if min_room_count:
            queryset = queryset.filter(min_room_count__gte=min_room_count)

        if max_floor:
            queryset = queryset.filter(max_floor__lte=max_floor)
     
        if min_floor:
            queryset = queryset.filter(min_floor__gte=min_floor)

        if max_floor_count:
            queryset = queryset.filter(max_floor_count__lte=max_floor_count)
     
        if min_floor_count:
            queryset = queryset.filter(min_floor_count__gte=min_floor_count)
        
        return queryset

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