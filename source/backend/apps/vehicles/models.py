import uuid
from django.db import models

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=100, null=False)
    owner = models.CharField(max_length=100, null=False)
    battery_installation_date = models.DateField(null=False)