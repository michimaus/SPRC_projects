from django.db import models


class CountryModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=128, unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        db_table = "COUNTRY_MODEL"


class CityModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)

    name = models.CharField(max_length=128, unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        db_table = "CITY_MODEL"


class TemperatureModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)

    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TEMPERATURE_MODEL"
