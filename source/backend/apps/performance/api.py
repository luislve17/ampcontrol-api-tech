from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from chargespot.models import Chargespot
from chargespot.serializers import ChargespotSerializer

from .utils import calculate_performance, request_contains 
from .serializers import WeightSerializer
from .models import Weight

@api_view(['GET', 'POST'])
def charge_performance(request):
    if request.method == "GET": return get_charge_performance(request)
    elif request.method == "POST": return post_performance_calc(request)

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

    # Save in performance table

    # Return info
    response_obj = {
        "vehicle_info": VehicleSerializer(vehicle).data,
        "chargespot_info": ChargespotSerializer(chargingspot).data,
        "weighting_info": performance['used_weight'],
        "vehicle_performance": round(performance['car_battery'], 3),
        "chargespot_performance":round(performance['chargespot'], 3),
        "overall_performance": round(performance['overall'], 3),
    }
    response_code = status.HTTP_200_OK
    return Response(response_obj, status=response_code)

def post_performance_calc(request):
    # Ensure request contains needed params
    expected_params = ['weight_id', 'vehicle_performance_weight', 'lat', 'lng']
    if not request_contains(request, expected_params, by="data"):
        response_obj = {"error": f"Missing params in query. Expected {expected_params}"}
        response_code = status.HTTP_400_BAD_REQUEST
        return Response(response_obj, status=response_code)
    
    # If so, get its values
    weight_id = request.data.get('weight_id')
    vehicle_performance_weight = request.data.get('vehicle_performance_weight')
    lat, lng = request.data.get('lat'), request.data.get('lng')

    
    # Search for matching objects from id's
    try:
        weight, created = Weight.objects.update_or_create(id=weight_id, defaults={
            "vehicle_performance_weight": vehicle_performance_weight,
            "lat":lat,
            "lng":lng})
    except Exception as e:
        response_obj = {"error": str(e)}
        response_code = status.HTTP_400_BAD_REQUEST
        return Response(response_obj, status=response_code)

    # Return info
    response_obj = {
        "status": "Weight created" if created else "Weight updated",
        "weight_info": WeightSerializer(weight).data,
    }
    response_code = status.HTTP_200_OK
    return Response(response_obj, status=response_code)