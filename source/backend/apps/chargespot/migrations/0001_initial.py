# Generated by Django 3.2.8 on 2021-10-11 19:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chargespot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location_hash', models.CharField(max_length=20)),
                ('last_maintenance_date', models.DateField()),
            ],
        ),
    ]