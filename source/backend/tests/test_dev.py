import pytest
from datetime import date
from dateutil.relativedelta import relativedelta

from vehicles.models import Vehicle 
from chargespot.models import Chargespot

@pytest.mark.django_db
def test_vehicle_battery_time_in_years():
    vehicle = Vehicle(brand='Test brand', owner='Test owner', battery_installation_date=date(2020, 5, 15))
    battery_age = relativedelta(date(2021, 4, 14), vehicle.battery_installation_date)
    battery_age_in_years = battery_age.months/12 + battery_age.years
    # print(battery_age_in_years)
    
    assert 0 < battery_age_in_years and battery_age_in_years < 1

@pytest.mark.django_db
def test_chargespot_maintenance_time_in_months():
    chargespot = Chargespot(
        name='Test chargepoint',
        lat=0,
        lng=0,
        last_maintenance_date=date(2019,8,30)
        )
    elapsed_time = relativedelta(date(2021, 4, 14), chargespot.last_maintenance_date)
    elapsed_time_in_months = elapsed_time.months + elapsed_time.years*12
    
    assert elapsed_time_in_months == 19