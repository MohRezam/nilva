from django.urls import path
from . import apis

urlpatterns = [
    path("weather/full/", apis.WeatherAPIView.as_view(), name="weather_api"),
]
