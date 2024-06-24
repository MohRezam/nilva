from django.contrib import admin
from .models import CurrentData, FutureHour, FutureDay

class FutureHourInline(admin.TabularInline):
    model = FutureHour

class FutureDayInline(admin.TabularInline):
    model = FutureDay

@admin.register(CurrentData)
class WeatherDataAdmin(admin.ModelAdmin):
    inlines = [FutureHourInline, FutureDayInline]
    list_display = ('location_name', 'date', 'latitude', 'longitude')
    search_fields = ('id', 'latitude', 'longitude')
    
