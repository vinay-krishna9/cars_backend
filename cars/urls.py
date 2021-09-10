from django.conf.urls import url
from cars import views

urlpatterns = [
    url(r'cars', views.carsApi),
    url('distinctyear', views.distinctYearApi),
    url('distinctfuel', views.distinctFuelApi),
    url('distinctsellertype', views.distinctSellerTypeApi),
    url('search', views.searchApi),
    url('filter', views.filterApi),
]
