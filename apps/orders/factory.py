import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'John'
    last_name = 'Cena'
    email = 'j.cena@gmail.com'
    phone = '+2431534679'
    message = 'Call me, when you have written this text'
    car_id = 4
