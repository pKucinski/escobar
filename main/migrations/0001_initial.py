# Generated by Django 4.0.5 on 2022-08-10 20:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='opis')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cena (zł)')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='opis')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cena (zł)')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='opis')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cena (zł)')),
            ],
        ),
        migrations.CreateModel(
            name='FunFacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.TextField(blank=True, null=True, verbose_name='fakt')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_start', models.TimeField(blank=True, null=True, verbose_name='Poniedziałek otwarcie')),
                ('monday_end', models.TimeField(blank=True, null=True, verbose_name='Poniedziałek zamknięcie')),
                ('monday_open', models.BooleanField(default=True, help_text='odznacz ', verbose_name='Czy otwarte')),
                ('tuesday_start', models.TimeField(blank=True, null=True)),
                ('tuesday_end', models.TimeField(blank=True, null=True)),
                ('tuesday_open', models.BooleanField(default=True)),
                ('wednesday_start', models.TimeField(blank=True, null=True)),
                ('wednesday_end', models.TimeField(blank=True, null=True)),
                ('wednesday_open', models.BooleanField(default=True)),
                ('thursday_start', models.TimeField(blank=True, null=True)),
                ('thursday_end', models.TimeField(blank=True, null=True)),
                ('thursday_open', models.BooleanField(default=True)),
                ('friday_start', models.TimeField(blank=True, null=True)),
                ('friday_end', models.TimeField(blank=True, null=True)),
                ('friday_open', models.BooleanField(default=True)),
                ('saturday_start', models.TimeField(blank=True, null=True)),
                ('saturday_end', models.TimeField(blank=True, null=True)),
                ('saturday_open', models.BooleanField(default=True)),
                ('sunday_start', models.TimeField(blank=True, null=True)),
                ('sunday_end', models.TimeField(blank=True, null=True)),
                ('sunday_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='opis')),
                ('price_small', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cena za małą pizze (zł)')),
                ('price_big', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cena za dużą pizze (zł)')),
            ],
        ),
    ]
