# Performance-based Electrical Vehicles Charging Monitoring System

## AMPCONTROL.io Technical test - Backend position

Affinity calculation backend system for vehicle - charging points interaction, based on the useful life of the vehicle's battery, the time elapsed since the last maintenance provided to the charging point and the custom tweaking of the performance metric calculation.

## API Reference

#### Calculates a performance metric that tells how good will this _chargespot_ be for this _vehicle_ in particular, giving in the response the info about the entities, the weight used for this performance calculation and the performance result.

```http
  GET /api/performance/
```

| Parameter         | Type                    | Description                |
| :---------------- | :---------------------- | :------------------------- |
| `chargingspot_id` | `UUID-formatted string` | **Required**. Your API key |
| `vehicle_id`      | `UUID-formatted string` | **Required**. Your API key |

**Response**

```json
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

#### Performs a `CREATE_OR_UPDATE` operation using as search pivot the provided name, and handling the definition or updating of a certain performance calculation weighting.

```http
  POST /api/performance/
```

| Parameter                    | Type     | Description                                                                                                |
| :--------------------------- | :------- | :--------------------------------------------------------------------------------------------------------- |
| `weight_name`                | `string` | **Required**. Identifier for weight reference                                                              |
| `vehicle_performance_weight` | `float`  | **Required**. Statistical weight assigned to vehicle performance value for overall performance calculation |
| `lat`                        | `float`  | **Required**. Latitude reference for weight ubication                                                      |
| `lng`                        | `float`  | **Required**. Longitude reference for weight ubication                                                     |

**Response**

```json
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

## Documentation

For each Django app, there will be a README.md file for further info about implementation details.
Currently available for:

- APP:UTILS
- APP:VEHICLES
- APP:CHARGESPOT
- APP:PERFORMANCE

## Deployment

Needs:

- Docker & Docker compose
- Make (as in GNU make tool)

To deploy this project, after cloning it to your local, naviagte to the root path and use the `makefile` to build-up and/or run the project's server:

```bash
  make docker-up-dev
```

or

```bash
  make docker-up-rebuild-dev # Useful for developing and installing new dependencies
```

## Maintenance

### From Django Admin

After getting the project up and running, you have at your disposal the **Django admin dashboard** (`http://localhost:8000/admin`). From here the credentials (configurable from `/config/backend.env`) to access are:

```
username: devuser
password: devpass
```

From here, the revision, audit and maintenance of the models and endpoints are handled easily. All three apps's models are available to check at detail. Additionally, from the installed middleware `drf_api_logger`, the developer can check the health, response time, execution and user blame of the API usage.

### From project structure

For developing purposes, **you will also need `pipenv` installed** to handle the dependencies, package managing and Django commands usage.

Thanks to the structure created by Django, the implementation and maintenance of the source code is independent from the distribution of the project. When implementing a new functionality it will be enough to use startapp; and of the existing ones, its modification can be managed by reviewing the documented routes.

Assuming you already did `pipenv install` and `pipenv shell`, for new apps creation:

1. Navigate to the `apps` folder in the project
2. Since `manage.py` will be in upper folders, run `python ../../manage.py startapp <new_app_name>`
3. Code

## Running Tests

Unittest are already configured on build-up for the project. Checking `start.sh` at root path of the project, the line handling the tests simply runs `pytest`.

Now, for specific testing, you would need to enter into the docker instance and run specific pytest commands

For **all** tests, the project is already configured with pytest-django package and expects to follow the naming convention defined in `pytest.ini`, and coming from the `source/backend/tests/` folder.
