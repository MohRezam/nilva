# Generated by Django 5.0.6 on 2024-06-24 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location_name', models.CharField(max_length=255)),
                ('temp_now', models.FloatField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('weather_icon_type', models.CharField(max_length=255)),
                ('wind_speed', models.FloatField()),
                ('wind_deg', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('sunrise', models.DateTimeField()),
                ('sunset', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FutureDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('weather_icon_type', models.CharField(max_length=255)),
                ('weather_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='future_days', to='general.currentdata')),
            ],
        ),
        migrations.CreateModel(
            name='FutureHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('temp', models.FloatField()),
                ('weather_icon_type', models.CharField(max_length=255)),
                ('weather_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='future_hours', to='general.currentdata')),
            ],
        ),
    ]