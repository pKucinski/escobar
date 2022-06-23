from django.forms import ModelForm
from.models import Pizza, Drink, Dish, Alcohol


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'description', 'price_small', 'price_big']


class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'description', 'price']


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price']


class AlcoholForm(ModelForm):
    class Meta:
        model = Alcohol
        fields = ['name', 'description', 'price']

