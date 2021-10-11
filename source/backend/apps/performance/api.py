from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from vehicles.models import Vehicle
from chargespot.models import Chargespot
from .utils import calculate_performance, request_contains 

@api_view(['GET', 'POST'])
def charge_performance(request):
    if request.method == "GET": return get_charge_performance(request)
    elif request.method == "POST": return update_charge_performance(request)

def get_charge_performance(request):
    # Ensure request contains needed params
    expected_params = ['vehicle_id', 'chargingspot_id']
    if not request_contains(request, expected_params):
        response_obj = {"error": f"Missing params in query. Expected {expected_params}"}
        response_code = status.HTTP_400_BAD_REQUEST
        return Response(response_obj, status=response_code)
    
    # If so, get its values
    vehicle_id = request.query_params.get('vehicle_id')
    chargingspot_id = request.query_params.get('chargingspot_id')
    
    # Search for matching objects from id's
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        chargingspot = Chargespot.objects.get(id=chargingspot_id)
    except Exception as e:
        response_obj = {"error": str(e)}
        response_code = status.HTTP_400_BAD_REQUEST
        return Response(response_obj, status=response_code)

    # Calculate performance
    performance = calculate_performance(vehicle, chargingspot)
    # Return info
    response_obj = {
        "vehicle_performance": round(performance['car_battery'], 3),
        "chargespot_performance":round(performance['chargespot'], 3),
        "final_performance": round(performance['final'], 3),
    }

    response_code = status.HTTP_200_OK
    return Response(response_obj, status=response_code)

def update_charge_performance(request):
    return Response({"msg":"dev_POST_ok"}, status.HTTP_200_OK)