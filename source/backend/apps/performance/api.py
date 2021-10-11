from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from vehicles.models import Vehicle
from chargespot.models import Chargespot

@api_view(['GET', 'POST'])
def charge_performance(request):
    if request.method == "GET": return get_charge_performance(request)
    elif request.method == "POST": return update_charge_performance(request)

def get_charge_performance(request):
    return Response({"msg":"dev_GET_ok"}, status.HTTP_200_OK)

def update_charge_performance(request):
    return Response({"msg":"dev_POST_ok"}, status.HTTP_200_OK)

def calculate_performance(vehicle: Vehicle, chargespot: Chargespot):
    pass