from django.db import models


# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True, db_column="Id")
    name = models.CharField(max_length=255, unique=True, db_column="Name")
    capital = models.CharField(max_length=255, blank=False, db_column="Capital")
    languages = models.CharField(max_length=1000, blank=False, db_column="Languages")
    area_in_km2 = models.CharField(max_length=255, blank=False, db_column="Area(km2)")
    population = models.CharField(max_length=255, blank=False, db_column="Population")
    density_per_km2 = models.CharField(max_length=255, blank=False, db_column="Density(/km2)")
    time_zone = models.CharField(max_length=255, blank=False, db_column="Time_Zone")

    class Meta:
        db_table = "Country"

    def __str__(self):
        return self.name
