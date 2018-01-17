from django.db import models
from django.urls import reverse


class Carrier(models.Model):
    name = models.CharField(max_length=500)
    register_date = models.DateField()

    def get_absolute_url(self):
        return reverse('manager:carriers_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Trip(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    departure_city = models.CharField(max_length=100)
    arrive_city = models.CharField(max_length=100)
    date = models.DateTimeField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.carrier) + ': ' + str(self.departure_city) + ' - ' + str(self.arrive_city) \
               + ' (' + str(self.date) + '). Tickets: ' + str(self.quantity)


class Order(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=12)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.carrier) + ': ' + str(self.name) + ' ' + str(self.surname) + ' - ' + str(self.email) \
               + ' (' + str(self.phone) + '). Passengers: ' + str(self.quantity)
