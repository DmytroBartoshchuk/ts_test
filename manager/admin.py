from django.contrib import admin
from .models import Carrier, Order, Trip

admin.site.register(Carrier)
admin.site.register(Trip)
admin.site.register(Order)
