import django.core.exceptions

from .models import Country
from django.core import serializers
from django.http import JsonResponse, HttpResponseNotFound
import json


# Create your views here.
def countries_all_view(request):
    if request.method == "GET":
        countries = Country.objects.all()
        serializer = serializers.serialize("json", countries)
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})


def countries_top_view(request, my_top):
    if request.method == "GET":
        try:
            countries = Country.objects.all().order_by('-' + my_top)[:10]
        except django.core.exceptions.FieldError:
            return HttpResponseNotFound('<h1>Not found</h1>')
        serializer = serializers.serialize("json", countries, fields=('id', 'name', my_top))
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})


def countries_time_view(request, my_time):
    if request.method == "GET":
        countries = Country.objects.filter(time_zone=my_time)
        if not countries:
            return HttpResponseNotFound('<h1>Not found</h1>')
        serializer = serializers.serialize("json", countries, fields=('id', 'name', 'time_zone'))
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})


def countries_language_view(request, my_language):
    if request.method == "GET":
        countries = Country.objects.all()
        my_list = list()
        for country in countries:
            languages_lower = [language.lower() for language in country.languages.split(" ")]
            if my_language.lower() in languages_lower:
                my_list.append(country.id)
        countries = Country.objects.filter(pk__in=my_list)
        if not countries:
            return HttpResponseNotFound('<h1>Not found</h1>')
        serializer = serializers.serialize("json", countries, fields=('id', 'name', 'languages'))
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})


def countries_government_view(request, my_government):
    if request.method == "GET":
        countries = Country.objects.all()
        my_list = list()
        for country in countries:
            government_lower = [government.lower() for government in country.government.split(" ")]
            if my_government in government_lower:
                my_list.append(country.id)
        countries = Country.objects.filter(pk__in=my_list)
        if not countries:
            return HttpResponseNotFound('<h1>Not found</h1>')
        serializer = serializers.serialize("json", countries, fields=('id', 'name', 'government'))
        return JsonResponse(json.loads(serializer), safe=False, json_dumps_params={'indent': 2})
