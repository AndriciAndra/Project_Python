from django.urls import path
from country_api.views import *

urlpatterns = [
    path('', countries_all_view),
    path('top-10-countries-<str:my_top>', countries_top_view),
    path('time-zone/<str:my_time>', countries_time_view),
    path('language-<str:my_language>', countries_language_view),
]
