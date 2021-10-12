# APP:VEHICLES

Contains the general abstraction of the 'vehicle' object, focusing on its battery age/usage.

## Current use:

- **Model definition:**

App is used as object definer within model class, for future handling in requests and database.
Structure is as follows:

|           field           |                                  desc                                  |        values         |
| :-----------------------: | :--------------------------------------------------------------------: | :-------------------: |
|            id             |                  UUID identifier for each data entry                   | UUID formatted string |
|           brand           |                              Car's brand                               |        string         |
|           owner           |                              Car's owner                               |        string         |
| battery_installation_date | Date of when battery was supplied/installed to this particular vehicle |        string         |

## Source code of interest:

- `./admin`: Admin configuration to handle model from Django's admin dashboard
- `./models`: Database/Model definition of the Vehicle entity
- `./serializers`: Format definition for vehicle instance handling at API responses
