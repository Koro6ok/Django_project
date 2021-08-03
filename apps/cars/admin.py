from django.contrib import admin

# Register your models here.
from apps.cars.models import Cars, Picture, Color, Brand, Model, Property


admin.site.register(Cars)
admin.site.register(Picture)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Property)