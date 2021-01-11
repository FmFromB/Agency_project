from django.urls import path, include
from .views import *

urlpatterns = [

    #home urls
    path('', HomeListView.as_view(), name='home'),

    #offer urls
    path('offers', OffersListView.as_view(), name='offers'),
    path('detail/<int:pk>', OffersDetailView.as_view(), name='detail_page'),
    path('add_offer', OfferCreateView.as_view(), name='add_offer'),
    path('update_offer/<int:pk>', OfferUpdateView.as_view(), name='update_offer'),
    path('delete_offer/<int:pk>', OfferDeleteView.as_view(), name='delete_offer'),
    
    #reqs urls
    path('reqs', ReqsListView.as_view(), name='reqs'),
    path('detail_req/<int:pk>', ReqsDetailView.as_view(), name='detail_req_page'),
    path('add_req', ReqsCreateView.as_view(), name='add_req'),
    path('update_req/<int:pk>', ReqsUpdateView.as_view(), name='update_req'),
    path('delete_req/<int:pk>', ReqsDeleteView.as_view(), name='delete_req'),

    #login/logout urls
    path('login_page', StormwindLoginView.as_view(), name='login_page'),
    path('register_page', RegisterUserView.as_view(), name='register_page'),
    path('logout_page', StormwindLogoutView.as_view(), name='logout_page'),
]
