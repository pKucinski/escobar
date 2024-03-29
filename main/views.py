from django.shortcuts import render, get_object_or_404, redirect
from .models import Pizza, Meal, Vodka, Drink, Shot, Coffee, Beer, OpeningHours, FunFacts
from .forms import PizzaForm, MealForm, ShotForm, VodkaForm, BeerForm, DrinkForm, CoffeeForm, OpeningHoursForm
from django.contrib.auth.decorators import login_required


def index(request):
    fun_facts = FunFacts.objects.all()
    pizza = Pizza.objects.all()
    meal = Meal.objects.all()
    shot = Shot.objects.all()
    drink = Drink.objects.all()
    beer = Beer.objects.all()
    vodka = Vodka.objects.all()
    coffee = Coffee.objects.all()
    opening_hours = OpeningHours.objects.all()

    return render(request, 'index.html', {'pizza': pizza,'beer': beer,'vodka': vodka,'coffee': coffee, 'meal': meal, 'shot': shot, 'drink': drink, 'opening_hours': opening_hours, 'fun_facts': fun_facts})


@login_required()
def new_position(request):
    current_url = request.build_absolute_uri()
    new_product = True

    if "drink" in current_url:
        form = DrinkForm(request.POST or None, request.FILES or None)

    elif "zab" in current_url:
        form = MealForm(request.POST or None, request.FILES or None)

    elif "piwo" in current_url:
        form = BeerForm(request.POST or None, request.FILES or None)

    elif "pizza" in current_url:
        form = PizzaForm(request.POST or None, request.FILES or None)

    elif "kawa" in current_url:
        form = CoffeeForm(request.POST or None, request.FILES or None)

    elif "wodka" in current_url:
        form = VodkaForm(request.POST or None, request.FILES or None)

    else:
        form = ShotForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('/#menu')

    return render(request, 'formularz_pozycji.html', {'form': form, 'new_product': new_product})


@login_required()
def edit(request,id):
    current_url = request.build_absolute_uri()
    new_product = False

    if "drink" in current_url:
        object = get_object_or_404(Drink, pk=id)
        form = DrinkForm(request.POST or None, request.FILES or None, instance=object)

    elif "piwo" in current_url:
        object = get_object_or_404(Beer, pk=id)
        form = BeerForm(request.POST or None, request.FILES or None, instance=object)

    elif "kawa" in current_url:
        object = get_object_or_404(Coffee, pk=id)
        form = CoffeeForm(request.POST or None, request.FILES or None, instance=object)

    elif "wodka" in current_url:
        object = get_object_or_404(Vodka, pk=id)
        form = VodkaForm(request.POST or None, request.FILES or None, instance=object)

    elif "cos_na_zab" in current_url:
        object = get_object_or_404(Meal, pk=id)
        form = MealForm(request.POST or None, request.FILES or None, instance=object)

    elif "pizza" in current_url:
        object = get_object_or_404(Pizza, pk=id)
        form = PizzaForm(request.POST or None, request.FILES or None, instance=object)

    else:
        object = get_object_or_404(Shot, pk=id)
        form = ShotForm(request.POST or None, request.FILES or None, instance=object)

    if form.is_valid():
        form.save()
        return redirect('/#menu')

    return render(request, 'formularz_pozycji.html', {'form': form, 'id':id, 'new_product': new_product})


@login_required()
def delete(request,id):

    current_url = request.build_absolute_uri()

    if "drink" in current_url:
        form = get_object_or_404(Drink, pk=id)

    elif "zab" in current_url:
        form = get_object_or_404(Meal, pk=id)

    elif "beer" in current_url:
        form = get_object_or_404(Beer, pk=id)

    elif "kawa" in current_url:
        form = get_object_or_404(Coffee, pk=id)

    elif "wodka" in current_url:
        form = get_object_or_404(Vodka, pk=id)

    elif "pizza" in current_url:
        form = get_object_or_404(Pizza, pk=id)

    else:
        form = get_object_or_404(Shot, pk=id)

    if request.method == "POST":
        form.delete()
        return redirect('/#menu')

    return render(request, 'potwierdz.html', {'form': form})


@login_required()
def edit_hours(request, id):
    current_url = request.build_absolute_uri()

    object = get_object_or_404(OpeningHours, pk=id)
    form = OpeningHoursForm(request.POST or None, request.FILES or None, instance=object)


    if form.is_valid():
        form.save()
        return redirect('/#menu')

    return render(request, 'edycja_godzin_otwarcia.html', {'form': form, 'id': id})