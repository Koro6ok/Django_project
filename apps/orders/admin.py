from django.contrib import admin

# Register your models here.
from apps.orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('email', 'car', 'status', )


admin.site.register(Order, OrderAdmin)