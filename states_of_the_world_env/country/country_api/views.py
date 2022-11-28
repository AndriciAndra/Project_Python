from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serializers import CountrySerializer


# Create your views here.
class CountriesListApiView(APIView):
    def get(self, *args, **kwargs):
        countries = Country.objects.all()
        print(countries)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
