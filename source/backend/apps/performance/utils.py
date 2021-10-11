from math import ceil
from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
def calculate_performance(vehicle, chargespot):
    battery_age_perf = lambda age_in_years: max([0, -0.3*age_in_years + 1])
    chargespot_time_since_maintenance_perf = lambda last_maintenance_in_months: max([0, -0.3*ceil(0.5*last_maintenance_in_months) + 1.3])

    battery_age = relativedelta(date.today(), vehicle.battery_installation_date)
    time_since_last_maintenance = relativedelta(date.today(), chargespot.last_maintenance_date)

    car_battery_years = battery_age.years + battery_age.months/12
    chargespot_elapsed_months_since_maintenance = time_since_last_maintenance.years*12 + time_since_last_maintenance.months
    car_battery_performance = battery_age_perf(car_battery_years)
    chargespot_performance = chargespot_time_since_maintenance_perf(chargespot_elapsed_months_since_maintenance)
    final_performance = (car_battery_performance + chargespot_performance) / 2
    return {
        'car_battery':car_battery_performance,
        'chargespot': chargespot_performance,
        'final': final_performance
    }

def request_contains(request, expected_params, by='query_params'):
    if by == 'query_params':
        key_set = set(request.query_params.keys())
    elif by == 'data':
        key_set = set(request.data.keys())

    expected_params = set(expected_params)
    return expected_params.issubset(key_set)