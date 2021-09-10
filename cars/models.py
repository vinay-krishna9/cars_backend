from django.db import models

# Create your models here.


class Cars(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    selling_price = models.CharField(max_length=255)
    km_driven = models.CharField(max_length=255)
    fuel = models.CharField(max_length=255)
    seller_type = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    mileage = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    max_power = models.CharField(max_length=255)
    torque = models.CharField(max_length=255)
    seats = models.CharField(max_length=255)
