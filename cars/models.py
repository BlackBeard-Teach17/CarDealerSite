import datetime
from django.db import models
from django.urls import reverse


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100, )
    CATEGORY = (
        ('New', 'New'),
        ('Used', 'Used')
    )
    category = models.CharField(max_length=50, choices=CATEGORY)
    image_main = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', blank=True)

    kilometers = models.IntegerField()
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
    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    YEAR_CHOICES = [(r,r) for r in range(2005, datetime.date.today().year + 1)]
    year = models.IntegerField('year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    power = models.IntegerField()
    fuel_type = models.CharField(max_length=50, choices=FUEL)
    fuel_tank_ = models.IntegerField(default=10)
    price = models.DecimalField(models.Min(1000))
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'car_id': self.id})
