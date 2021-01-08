from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Realtor)
admin.site.register(Offer)
admin.site.register(Requirement)
admin.site.register(Deal)

# Register your models here.
