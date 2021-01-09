from django.urls import path, include
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views
from .views import *

urlpatterns = [
    #Auth urls
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('auth/token', ObtainAuthToken, name='token'),
    #path('auth/logout', Logout.as_view())

    #Client urls
    path('clients/<int:pk>', ClientRetrieveView.as_view()),
    path('clients/update/<int:pk>', ClientUpdateView.as_view()),
    path('clients/new', ClientCreateView.as_view()),
    path('clients/all', ClientListView.as_view()),

    #Realor urls
    path('realtors/<int:pk>', RealtorRetrieveView.as_view()),
    path('realtors/update/<int:pk>', RealtorUpdateView.as_view()),
    path('realtors/new', RealtorCreateView.as_view()),
    path('realtors/all', RealtorListView.as_view()),

    #Offer urls
    path('offers/<int:pk>', OfferRetrieveView.as_view()),
    path('offers/update/<int:pk>', OfferUpdateView.as_view()),
    path('offers/new', OfferCreateView.as_view()),
    path('offers/all', OfferListView.as_view()),

    #Requirement urls
    path('requirements/<int:pk>', RequirementRetrieveView.as_view()),
    path('requirements/update/<int:pk>', RequirementUpdateView.as_view()),
    path('requirements/new', RequirementCreateView.as_view()),
    path('requirements/all', RequirementListView.as_view()),

    #Deal urls
    path('deals/<int:pk>', DealRetrieveView.as_view()),
    path('deals/update/<int:pk>', DealUpdateView.as_view()),
    path('deals/new', DealCreateView.as_view()),
    path('deals/all', DealListView.as_view()),
]