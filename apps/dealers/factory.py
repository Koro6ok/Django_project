import factory

class CarDealersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Dealers'

    title = 'factory_dealer'