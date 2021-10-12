import uuid
from django.db import models

class Weight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    vehicle_performance_weight = models.FloatField(null=False)
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
