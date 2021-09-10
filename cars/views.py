from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import filters

from cars.models import Cars
from cars.serializers import CarsSerializers, YearSerializers, FuelSerializers, SellerTypeSerializers


@csrf_exempt
def carsApi(request):
    if request.method == 'GET':
        cars = Cars.objects.all()
        cars_serializers = CarsSerializers(cars, many=True)
        return JsonResponse(cars_serializers.data, safe=False)


@csrf_exempt
def distinctYearApi(request):
    if request.method == 'GET':
        cars = Cars.objects.values('year').distinct()
        cars_serializers = YearSerializers(cars, many=True)
        return JsonResponse(cars_serializers.data, safe=False)


@csrf_exempt
def distinctFuelApi(request):
    if request.method == 'GET':
        cars = Cars.objects.values('fuel').distinct()
        cars_serializers = FuelSerializers(cars, many=True)
        return JsonResponse(cars_serializers.data, safe=False)


@csrf_exempt
def distinctSellerTypeApi(request):
    if request.method == 'GET':
        cars = Cars.objects.values('seller_type').distinct()
        cars_serializers = SellerTypeSerializers(cars, many=True)
        return JsonResponse(cars_serializers.data, safe=False)


@csrf_exempt
def searchApi(request):
    if request.method == 'POST':
        search_data = JSONParser().parse(request)
        manufacturer = Cars.objects.filter(
            name__contains=search_data['search']).values()
        return JsonResponse({"result": list(manufacturer)}, safe=False)


@csrf_exempt
def filterApi(request):
    if request.method == 'POST':
        search_data = JSONParser().parse(request)
        filtered = Cars.objects.filter(
            year__contains=search_data['year']).filter(
            fuel__contains=search_data['fuel']).filter(
            seller_type__contains=search_data['seller_type']).values()
        return JsonResponse({"result": list(filtered)}, safe=False)
