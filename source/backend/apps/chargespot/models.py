import uuid
from django.db import models

class Chargespot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    location_hash = models.CharField(max_length=20, null=False)
    last_maintenance_date = models.DateField(null=False)