from rest_framework import serializers

class TemperatureSerializer(serializers.Serializer):
    now = serializers.FloatField(required=False)
    min = serializers.FloatField()
    max = serializers.FloatField()

class WeatherIconSerializer(serializers.Serializer):
    icon_type = serializers.CharField(max_length=50)

class WindSerializer(serializers.Serializer):
    speed = serializers.FloatField()
    deg = serializers.FloatField()

class HourlyForecastSerializer(serializers.Serializer):
    date = serializers.IntegerField()
    temp = serializers.FloatField()
    weather = WeatherIconSerializer()

class DailyForecastSerializer(serializers.Serializer):
    date = serializers.IntegerField()
    temp = TemperatureSerializer()
    weather = WeatherIconSerializer()

class WeatherSerializer(serializers.Serializer):
    date = serializers.IntegerField()
    location_name = serializers.CharField(max_length=100)
    temp = TemperatureSerializer()
    weather = WeatherIconSerializer()
    wind = WindSerializer()
    humidity = serializers.IntegerField()
    pressure = serializers.IntegerField()
    sunrise = serializers.IntegerField()
    sunset = serializers.IntegerField()
    future_hours = HourlyForecastSerializer(many=True)
    future_days = DailyForecastSerializer(many=True)

