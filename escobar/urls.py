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
from main.views import index, new_position, edit, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('nowe_danie', new_position),
    path('nowa_pizza', new_position),
    path('nowy_alkohol', new_position),
    path('nowy_drink', new_position),
    path('edytuj_danie/<int:id>/', edit),
    path('edytuj_pizza/<int:id>/', edit),
    path('edytuj_alkohol/<int:id>/', edit),
    path('edytuj_drink/<int:id>/', edit),
    path('usun_danie/<int:id>/', delete),
    path('usun_pizza/<int:id>/', delete),
    path('usun_alkohol/<int:id>/', delete),
    path('usun_drink/<int:id>/', delete),
]
