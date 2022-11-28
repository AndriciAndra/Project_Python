from django.urls import path
from .views import CountriesListApiView

urlpatterns = [path('getAll', CountriesListApiView.as_view())]
