# APP:PERFORMANCE

Contains the implementation logic to estimate the affinity (defined as _performance_) for a particular vehicle to correctly charge using a particular chargespot.
The application handles the fetching of this metric (via GET operation), the tweaking of the averaging procedure creating custom reference weights (via POST operation) and all the in-between labor of handling the communication with `Vehicle` and `Chargespot` apps.

## Current use:

- **Model definition:**

App is used as object definer within model class, for future handling in requests and database.
Structure is as follows:

|           field            |                                       desc                                       |        values         |
| :------------------------: | :------------------------------------------------------------------------------: | :-------------------: |
|             id             |                       UUID identifier for each data entry                        | UUID formatted string |
|            name            |                Identifier name for human-readable identification                 |        string         |
| vehicle_performance_weight | Statistical weight for the performance calculated from the vehicle's battery age |         float         |
|            lat             |                       weight reference location's latitus                        |         float         |
|            lng             |                      weight reference location's longitude                       |         float         |

- **Endpoint definition:**

  - `/performance/`

    1. `GET`:
       Expects both `Vehicle` and a `Chargespot` UUID-formatted strings. From this, the endpoint will calculate a performance metric that tells how good will this _chargespot_ be for this _vehicle_ in particular, giving in the response the info about the entities, the weight used for this performance calculation and the performance result.

       **Example:**

       ```
       # GET
       curl --location --request GET 'localhost:8000/api/performance/?chargingspot_id=5851e8f3-03f4-4a96-866a-bde545dea7a0&vehicle_id=c5159d89-dc8d-453f-abea-31f5b070bb45'

       # Response:
       {
            "vehicle_info": {
                "brand": "BMW",
                "owner": "John",
                "battery_installation_date": "2019-11-12"
            },
            "chargespot_info": {
                "name": "Near the Sea Station - Peru",
                "lat": -12.118855,
                "lng": -77.043028,
                "last_maintenance_date": "2019-09-18"
            },
            "weighting_info": {
                "from": "Peru law performance weight",
                "vehicle_performance_weight": 0.75
            },
            "vehicle_performance": 0.425,
            "chargespot_performance": 0,
            "overall_performance": 0.159
        }
       ```

    2. `POST`
       Expects the following fields in the request body: `weight_name, vehicle_performance_weight, lat, lng`, representing the human-readable weight name, its performance calculation value and its referencial ubication. From this, a `CREATE_OR_UPDATE` operation will execute using as search pivot the provided name, and handling the definition or updating of a certain performance calculation weighting.

       **Example:**

       ```
       # POST
       curl --location --request POST 'localhost:8000/api/performance/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "weight_name":"USA East Coast Standar weight",
            "vehicle_performance_weight":0.51,
            "lat":36.832383,
            "lng":-77.393799
        }'

        # Response

        {
            "status": "Weight updated",
            "weight_info": {
                "name": "USA East Coast Standar weight",
                "vehicle_performance_weight": 0.51,
                "lat": 36.832383,
                "lng": -77.393799
            }
        }
       ```

- **Estimation definition:**

The idea behind the whole project is to define a geographic-based preference system for a specific client to recommend. Based on this, consuming the endpoint could point in the right direction to where is better for a certain vehicle to recharge. Changing the performance metrics for something more precise and involving more variables will be easy enough and would have the option to customize according to the creation of weights.

The current performance calculation uses:

- Vehicle's battery life until present (in years)
- Chargespot's time since last maintenance (in months)

And draws two math functions (one for each) in other to represent its decay in time. For a more precise intuition of these, you can check `/extras` folder on the project's root path. From this times, a basic averaging calculation is performed, depending on the weight assigned to perform it.

How does the system knows what weight to use? Using the **chargespot** location, the system itearates over all available weighting definitions and returns the nearest one from the **chargespot**, using it's value to finish the performance metric as follows:

```
vehicle_performance = math_perf_function_for_vehicle(vehicle)
chargespot_performance = math_perf_function_for_chargespot(chargespot)

W = selected weight definition (from nearest reference to current chargespot)

overall_performance = [ W * vehicle_performance + (1 - W) * chargespot_performance ] / 2
```

## Source code of interest:

- `./admin`: Admin configuration to handle model from Django's admin dashboard
- `./api`: Core definition of single implemented enpoint handling GET & POST requests
- `./models`: Database/Model definition of the Weight entity
- `./serializers`: Format definition for chargespot instance handling at API responses
- `./url`: Definition of the base `'/'` route for endpoint consuming
- `./utils`: Contains the core implementation of the performance metric calculation, besides of additional utilities like request arguments revision.
