from django.db.models import fields
from rest_framework import serializers
from cars import models
from cars.models import Cars


class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('name', 'year', 'selling_price', 'km_driven', 'fuel', 'seller_type',
                  'transmission', 'owner', 'mileage', 'engine', 'max_power', 'torque', 'seats')


class YearSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('year', )


class FuelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('fuel', )


class SellerTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('seller_type', )
