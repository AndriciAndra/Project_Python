from .models import Country
from django.core import serializers
from django.http import JsonResponse
import json


# Create your views here.
def countries_all_view(request):
    if request.method == "GET":
        countries = Country.objects.all()
        serializer = serializers.serialize("json", countries)
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})


def countries_top_view(request, my_top):
    if request.method == "GET":
        countries = Country.objects.all().order_by('-' + my_top)[:10]
        serializer = serializers.serialize("json", countries, fields=('id', 'name', my_top))
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})


def countries_time_view(request, my_time):
    if request.method == "GET":
        countries = Country.objects.filter(time_zone=my_time)
        serializer = serializers.serialize("json", countries, fields=('id', 'name', 'time_zone'))
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})


def countries_language_view(request, my_language):
    if request.method == "GET":
        countries = Country.objects.all()
        my_list = list()
        for country in countries:
            if my_language in country.languages:
                my_list.append(country.id)
        countries = Country.objects.filter(pk__in=my_list)
        serializer = serializers.serialize("json", countries)
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})
