from django.contrib import admin

# Register your models here.
from apps.dealers.models import Country, City, Dealers


class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'city',)
    autocomplete_fields = ('city',)
    search_fields = ('title',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    autocomplete_fields = ('country',)
    search_fields = ('name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', )
    search_fields = ('name', )


admin.site.register(Dealers, DealerAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)