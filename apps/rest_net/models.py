from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

# AUTH_USER_MODEL = get_user_model()


class Restik(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    staff = models.ManyToManyField(
        'rest_net.Staff'
    )

    country = models.OneToOneField(
        'rest_net.Country',
        on_delete=models.CASCADE,
        null=True
    )

    city = models.OneToOneField(
        'rest_net.City',
        on_delete=models.CASCADE,
        null=True
    )

    menu = models.ForeignKey(
        'rest_net.Menu',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Мережа ресторанів'
        verbose_name_plural = 'Мережі ресторанів'


class Staff(models.Model):
    ADMINISTRATOR = 'administrator'
    OFFICIANT = 'officiant'
    COOKER = 'cooker'
    CLEANER = 'cleaner'

    STAFF_POSITION = (
        (ADMINISTRATOR, "administrator"),
        (OFFICIANT, "officiant"),
        (COOKER, "cooker"),
        (CLEANER, "cleaner"),
    )

    full_name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=50,
        choices=STAFF_POSITION,
        blank=True
    )

    class Meta:
        verbose_name = 'Працівник'
        verbose_name_plural = 'Персонал'


class Country(models.Model):
    country = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'


class City(models.Model):
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'місто'
        verbose_name_plural = 'міста'


class Menu(models.Model):
    pass

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'


class Dish(models.Model):
    name = models.CharField(max_length=69)
    price = models.DecimalField
    weight = models.IntegerField
    menu = models.ForeignKey(
        'rest_net.Menu',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Стрва'
        verbose_name_plural = 'страви'