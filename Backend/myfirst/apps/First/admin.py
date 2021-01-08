from django.contrib import admin

from .models import Client, Realtor, Requirement, Offer, Deal

admin.site.register(Client)
admin.site.register(Realtor)
admin.site.register(Requirement)
admin.site.register(Offer)
admin.site.register(Deal)