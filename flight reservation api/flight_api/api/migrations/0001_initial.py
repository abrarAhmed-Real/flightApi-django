# Generated by Django 4.1.2 on 2023-04-09 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flightNumber", models.CharField(max_length=10)),
                ("operatingAirLines", models.CharField(max_length=20)),
                ("departureCirty", models.CharField(max_length=20)),
                ("ArrivalCity", models.CharField(max_length=20)),
                ("dateOfDeparture", models.DateField()),
                ("estimatedTimeOfDeparture", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Pessanger",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstName", models.CharField(max_length=10)),
                ("lastName", models.CharField(max_length=20)),
                ("middleName", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fligh",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.flight"
                    ),
                ),
                (
                    "pessanger",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.pessanger"
                    ),
                ),
            ],
        ),
    ]