# APP:CHARGESPOT

Contains the general abstraction of the 'chargespot' object, focusing on its maintainence schedule

## Current use:

- **Model definition:**

App is used as object definer within model class, for future handling in requests and database.
Structure is as follows:

|         field         |                          desc                          |        values         |
| :-------------------: | :----------------------------------------------------: | :-------------------: |
|          id           |          UUID identifier for each data entry           | UUID formatted string |
|         name          |   Identifier name for human-readable identification    |        string         |
|          lat          |             chargespot location's latitud              |         float         |
|          lng          |            chargespot location's longitude             |         float         |
| last_maintenance_date | Date of when chargespot was last underwent maintenance |       datetime        |

## Source code of interest:

- `./admin`: Admin configuration to handle model from Django's admin dashboard
- `./models`: Database/Model definition of the Chargespot entity
- `./serializers`: Format definition for chargespot instance handling at API responses
