# Generated by Django 3.2.7 on 2021-09-28 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('oaci', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('iata', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('grados_longitud', models.FloatField(default=0)),
                ('grados_latitud', models.FloatField(default=0)),
                ('altitud', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='Aeropuertos.aeropuerto')),
                ('origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='Aeropuertos.aeropuerto')),
            ],
        ),
    ]