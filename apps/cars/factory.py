import factory


class CarColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'Purpure'

