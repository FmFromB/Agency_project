from django.urls import path, include
from .views import *

urlpatterns = [
    path('offers', OffersListView.as_view(), name='offers'),
    path('detail/<int:pk>', OffersDetailView.as_view(), name='detail_page'),
    path('add_offer', add_offer, name='add_offer'),
]
