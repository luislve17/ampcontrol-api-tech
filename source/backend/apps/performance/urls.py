from django.urls import path, include

from . import api

urlpatterns = [
    path('', api.charge_performance, name='charge-performance'),
]