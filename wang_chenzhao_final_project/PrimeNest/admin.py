from django.contrib import admin

from .models import Agency, Tenant, Apartment, Period, Availability, Application, Rating, Review

admin.site.register(Agency)
admin.site.register(Tenant)
admin.site.register(Apartment)
admin.site.register(Period)
admin.site.register(Availability)
admin.site.register(Application)
admin.site.register(Rating)
admin.site.register(Review)