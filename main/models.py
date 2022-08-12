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


class Meal(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name


class Shot(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name

class Vodka(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="opis")
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name="Cena (zł)")

    def __str__(self):
        return self.name

class OpeningHours(models.Model):
    day_of_week = models.CharField(max_length=30, blank=False, null=False, verbose_name="Dzień tygodnia")
    day_start = models.TimeField(blank=True, null=True, verbose_name="Godzina otwarcie")
    day_end = models.TimeField(blank=True, null=True, verbose_name="Godzina zamknięcia")
    if_open = models.BooleanField(default=True, verbose_name="Czy otwarte", help_text="odznacz jeśli zamknięte")




