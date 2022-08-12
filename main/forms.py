from django.forms import ModelForm
from.models import Pizza, Drink, Meal, Shot, Coffee, Vodka, Beer, OpeningHours


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'description', 'price_small', 'price_big']


class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'description', 'price']


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'price']


class ShotForm(ModelForm):
    class Meta:
        model = Shot
        fields = ['name', 'description', 'price']


class CoffeeForm(ModelForm):
    class Meta:
        model = Coffee
        fields = ['name', 'description', 'price']


class VodkaForm(ModelForm):
    class Meta:
        model = Vodka
        fields = ['name', 'description', 'price']


class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'description', 'price']


class OpeningHoursForm(ModelForm):
    class Meta:
        model = OpeningHours
        fields = ['day_start', 'day_end', 'if_open']