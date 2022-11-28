from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name", "capital", "languages", "area_in_km2", "population", "density_per_km2", "time_zone"]
