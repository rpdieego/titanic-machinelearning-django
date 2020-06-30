# Generated by Django 3.0.7 on 2020-06-30 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=30)),
                ('passenger_age', models.CharField(max_length=30)),
                ('completed', models.BooleanField(default=False)),
                ('time_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
