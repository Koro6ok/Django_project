from django.contrib import admin

# Register your models here.
from apps.rest_net.models import Dish, Menu, Restik, Staff, Country, City

admin.site.register(Restik)
admin.site.register(Staff)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Menu)
admin.site.register(Dish)