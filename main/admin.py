from django.contrib import admin
from .models import Pizza, Meal, Shot, Drink, Coffee, Vodka, Beer, OpeningHours, FunFacts

admin.site.register(Pizza)
admin.site.register(Meal)
admin.site.register(Shot)
admin.site.register(Coffee)
admin.site.register(Vodka)
admin.site.register(Beer)
admin.site.register(Drink)
admin.site.register(OpeningHours)
admin.site.register(FunFacts)
