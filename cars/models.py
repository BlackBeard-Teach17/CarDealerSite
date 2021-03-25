import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone

from dealers.models import Dealer


# Create your models here.
class Car(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING, default=0)
    brand = models.CharField(max_length=100)
    CATEGORY = (
        ('New', 'New'),
        ('Used', 'Used')
    )
    category = models.CharField(max_length=50, choices=CATEGORY)
    image_main = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    kilometers = models.IntegerField(default=1000)
    TRANSMISSION = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    )

    FUEL = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric')
    )
    transmission = models.CharField(max_length=50, choices=TRANSMISSION, default='Manual')
    YEAR_CHOICES = [(r, r) for r in range(2005, datetime.date.today().year + 1)]
    year = models.IntegerField('year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    power = models.IntegerField(default=50)
    fuel_type = models.CharField(max_length=50, choices=FUEL, default='Petrol')
    fuel_tank_capacity = models.IntegerField(default=10)
    price = models.DecimalField(models.Min(1000), default=0.0, decimal_places=2, max_digits=10)
    description = models.TextField(default="Default description")
    vin = models.IntegerField(models.Min(11), default=123456)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'car_id': self.id})
