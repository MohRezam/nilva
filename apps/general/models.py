from django.db import models


class CurrentData(models.Model):
    date = models.BigIntegerField()
    location_name = models.CharField(max_length=255)
    temp_now = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    weather_icon_type = models.CharField(max_length=255)
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    sunrise = models.BigIntegerField()
    sunset = models.BigIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.location_name}:{self.latitude}--{self.longitude}"

class FutureHour(models.Model):
    weather_data = models.ForeignKey(CurrentData, related_name='future_hours', on_delete=models.CASCADE)
    date = models.BigIntegerField()
    temp = models.FloatField()
    weather_icon_type = models.CharField(max_length=255)
    
class FutureDay(models.Model):
    weather_data = models.ForeignKey(CurrentData, related_name='future_days', on_delete=models.CASCADE)
    date = models.BigIntegerField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    weather_icon_type = models.CharField(max_length=255)
    
    