from django.shortcuts import render, get_object_or_404, redirect
from .models import Pizza, Dish, Alcohol, Drink, Data, FunFacts
from .forms import PizzaForm, DishForm, AlcoholForm, DrinkForm
from django.contrib.auth.decorators import login_required


def index(request):
    fun_facts = FunFacts.objects.all()
    pizza = Pizza.objects.all()
    dish = Dish.objects.all()
    alcohol = Alcohol.objects.all()
    drink = Drink.objects.all()
    data = Data.objects.all()

    return render(request, 'index.html', {'pizza': pizza, 'dish': dish, 'alcohol': alcohol, 'drink': drink, 'data': data, 'fun_facts': fun_facts})


@login_required()
def new_position(request):
    current_url = request.build_absolute_uri()
    new_product = True

    if "drink" in current_url:
        form = DrinkForm(request.POST or None, request.FILES or None)

    elif "danie" in current_url:
        form = DishForm(request.POST or None, request.FILES or None)

    elif "pizza" in current_url:
        form = PizzaForm(request.POST or None, request.FILES or None)

    else:
        form = AlcoholForm(request.POST or None, request.FILES or None)

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

    elif "danie" in current_url:
        object = get_object_or_404(Dish, pk=id)
        form = DishForm(request.POST or None, request.FILES or None, instance=object)

    elif "pizza" in current_url:
        object = get_object_or_404(Pizza, pk=id)
        form = PizzaForm(request.POST or None, request.FILES or None, instance=object)

    else:
        object = get_object_or_404(Alcohol, pk=id)
        form = AlcoholForm(request.POST or None, request.FILES or None, instance=object)

    if form.is_valid():
        form.save()
        return redirect('/#menu')

    return render(request, 'formularz_pozycji.html', {'form': form, 'id':id, 'new_product': new_product})


@login_required()
def delete(request,id):

    current_url = request.build_absolute_uri()

    if "drink" in current_url:
        form = get_object_or_404(Drink, pk=id)

    elif "danie" in current_url:
        form = get_object_or_404(Dish, pk=id)

    elif "pizza" in current_url:
        form = get_object_or_404(Pizza, pk=id)

    else:
        form = get_object_or_404(Alcohol, pk=id)

    if request.method == "POST":
        form.delete()
        return redirect('/#menu')

    return render(request, 'potwierdz.html', {'form': form})