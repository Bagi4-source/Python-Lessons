# Generated by Django 5.0.2 on 2024-02-14 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('radius', models.FloatField(verbose_name='Радиус')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('mass', models.FloatField(verbose_name='Масса')),
            ],
        ),
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('planet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.planet', verbose_name='ID планеты')),
            ],
        ),
        migrations.AddField(
            model_name='planet',
            name='star_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.star', verbose_name='Радиус'),
        ),
    ]
