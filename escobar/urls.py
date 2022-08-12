"""escobar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index, new_position, edit, delete, edit_hours

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('nowy_cos_na_zab', new_position),
    path('nowa_pizza', new_position),
    path('nowa_kawa', new_position),
    path('nowe_piwo', new_position),
    path('nowa_wodka', new_position),
    path('nowy_kieliszek', new_position),
    path('nowy_drink', new_position),
    path('edytuj_cos_na_zab/<int:id>/', edit),
    path('edytuj_pizza/<int:id>/', edit),
    path('edytuj_kawa/<int:id>/', edit),
    path('edytuj_piwo/<int:id>/', edit),
    path('edytuj_wodka/<int:id>/', edit),
    path('edytuj_kieliszek/<int:id>/', edit),
    path('edytuj_drink/<int:id>/', edit),
    path('usun_cos_na_zab/<int:id>/', delete),
    path('usun_pizza/<int:id>/', delete),
    path('usun_kawa/<int:id>/', delete),
    path('usun_piwo/<int:id>/', delete),
    path('usun_wodka/<int:id>/', delete),
    path('usun_drink/<int:id>/', delete),
    path('usun_kieliszek/<int:id>/', delete),

    path('edycja_godzin_otwarcia/<int:id>/', edit_hours),
]
