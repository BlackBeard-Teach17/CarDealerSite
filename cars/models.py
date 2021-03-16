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

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'car_id':self.id})