from django.core.validators import MinValueValidator

from django.db import models


class FunFacts(models.Model):
    fact = models.TextField(blank=True, null=True, verbose_name="fakt")
    def __str__(self):
        return self.fact

class Pizza(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price_small = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena za małą pizze (zł)")
    price_big = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena za dużą pizze (zł)")

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name


class Alcohol(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name


class Data(models.Model):
    description = models.TextField(blank=False, null=False)
    phone = models.IntegerField(null=False, blank=False)
    monday_start = models.TimeField(blank=True, null=True)
    monday_end = models.TimeField(blank=True, null=True)
    tuesday_start = models.TimeField(blank=True, null=True)
    tuesday_end = models.TimeField(blank=True, null=True)
    wednesday_start = models.TimeField(blank=True, null=True)
    wednesday_end = models.TimeField(blank=True, null=True)
    thursday_start = models.TimeField(blank=True, null=True)
    thursday_end = models.TimeField(blank=True, null=True)
    friday_start = models.TimeField(blank=True, null=True)
    friday_end = models.TimeField(blank=True, null=True)
    saturday_start = models.TimeField(blank=True, null=True)
    saturday_end = models.TimeField(blank=True, null=True)
    sunday_start = models.TimeField(blank=True, null=True)
    sunday_end = models.TimeField(blank=True, null=True)



