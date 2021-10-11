# APP:UTILS

Contains general administration and operational source code that handles the backend configuration.

## Current use:

- **Ensure SuperUser command:**

Used in development environment for docker startup (check `source\start.sh`) in order to handle automatic _superuser_ creation if not present yet. Solves the problem of using `createsuperuser` and breaking the application if superuser was created before. The logic of this commmand is contained in `.management\commands\ensuresuperuser.py`, using expected django file naming/distribution.

## Source code of interest:

- `./utils/management/commands`: Folder for the commands' source code
