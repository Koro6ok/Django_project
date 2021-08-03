from django.db import models

# Create your models here.


class Cars(models.Model):

    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
    )

    dealer = models.ForeignKey(
        'dealers.Dealers',
        on_delete=models.CASCADE
    )

    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
    )

    property = models.ManyToManyField(
        'cars.Property'
    )


    ENGINE_THERMAL_ENGINE = 'Thermal engine'
    ENGINE_Electrical_ENGINE = 'Electrical engine'
    ENGINE_PHYSICAL_ENGINE = 'Physical engine'
    ENGINE_DEFAULT = 'No info'


    ENGINE_TYPE_CHOICES=(
        (ENGINE_THERMAL_ENGINE, 'Thermal engine'),
        (ENGINE_Electrical_ENGINE, 'Electrical engine'),
        (ENGINE_PHYSICAL_ENGINE, 'Physical engine'),
        (ENGINE_DEFAULT, 'No info'),
    )

    engine_type = models.CharField(
        max_length=40,
        choices=ENGINE_TYPE_CHOICES,
        default=ENGINE_DEFAULT,
    )

    POLLUTANT_CLASS_A = 'class A'
    POLLUTANT_CLASS_B = 'class B'
    POLLUTANT_CLASS_C = 'class C'
    POLLUTANT_CLASS_D = 'class D'
    POLLUTANT_CLASS_DEFAULT = 'No info'

    POLLUTANT_CLASSES_CHOICES = (
        (POLLUTANT_CLASS_A, 'class A'),
        (POLLUTANT_CLASS_B, 'class B'),
        (POLLUTANT_CLASS_C, 'class C'),
        (POLLUTANT_CLASS_D, 'class D'),
        (POLLUTANT_CLASS_DEFAULT, 'No info'),
    )

    pollutant_class = models.CharField(
        max_length=69,
        choices=POLLUTANT_CLASSES_CHOICES,
        default=POLLUTANT_CLASS_DEFAULT
    )

    price = models.IntegerField()

    FUEL_GAS = 'Gas'
    FUEL_DIESEL = 'Diesel'
    FUEL_ELECTRIC = 'Electic'
    FUEL_DEFAULT = 'No info'

    FUEL_TYPE_CHOICES = (
        (FUEL_GAS, 'Gas'),
        (FUEL_DIESEL, 'Diesel'),
        (FUEL_ELECTRIC, 'Electic'),
        (FUEL_DEFAULT, 'No info'),
    )

    fuel_type = models.CharField(
        max_length=30,
        choices=FUEL_TYPE_CHOICES,
        default=FUEL_DEFAULT,
    )

    ON_SALE = 'On sale'
    SOLD = 'Sold'
    ORDERED = 'Ordered'
    ARCHIVED = 'Archived'

    STATUS_TYPE_CHOICES = (
        (ON_SALE, 'On sale'),
        (SOLD, 'Sold'),
        (ORDERED, 'Ordered'),
        (ARCHIVED, 'Archived'),
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_TYPE_CHOICES,
        default=ARCHIVED,
    )

    doors = models.IntegerField()

    capacity = models.IntegerField()

    GEAR_MANUAL = 'Manual'
    GEAR_AUTOMATIC = 'Automatic'
    GEAR_ROBOT = 'Robot'
    GEAR_VARIATOR = 'Variator'
    GEAR_OTHER_TYPE = 'Other type of gearcase'
    GEAR_DEFAULT = 'No info'

    GEAR_CASE = (
        (GEAR_MANUAL, 'Manual'),
        (GEAR_AUTOMATIC, 'Automatic'),
        (GEAR_ROBOT, 'Robot'),
        (GEAR_VARIATOR, 'Variator'),
        (GEAR_OTHER_TYPE, 'Other type of gearcase'),
        (GEAR_DEFAULT, 'No info'),
    )

    gear_case = models.CharField(
        max_length=40,
        choices=GEAR_CASE,
        default=GEAR_DEFAULT,
    )

    numbers = models.PositiveIntegerField()

    slug = models.SlugField(max_length=255)

    sitting_place = models.PositiveIntegerField()

    first_registration_date = models.DateField(
        auto_now=False,
        auto_now_add=True,
    )

    engine_power = models.PositiveIntegerField()


    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.model.brand} {self.model}'


class Picture(models.Model):

    position = models.CharField(max_length=40)

    metadata = models.TextField(
        null=True,
        blank=True,
    )

    url = models.ImageField(
        upload_to='car_pictures',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return self.metadata


class Color(models.Model):

    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class Model(models.Model):

    name = models.CharField(max_length=60)

    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.name

class Property(models.Model):

    CATEGORY_ECONOM = 'Econom'
    CATEGORY_COMFORT = 'Comfort'
    CATEGORY_BUSINESS = 'Business'

    CATEGORY_CHOICES = (
        (CATEGORY_ECONOM, 'Econom'),
        (CATEGORY_COMFORT, 'Comfort'),
        (CATEGORY_BUSINESS, 'Business'),
    )

    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_ECONOM,
    )

    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name