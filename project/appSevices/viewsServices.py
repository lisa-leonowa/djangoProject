from django.http import HttpResponse
from django.shortcuts import render # библиотека для обработки запросов

from appSevices.Services import get_values
from appSevices.formsServices import NewServices, UpdateServices, SearchServices


def newSevices(request):
    if request.method == "POST":  # обработка POST запроса
        userform = NewServices(request.POST)
        values = get_values(userform)  # данные из формы
        return HttpResponse(values)
    else:  # обработка GET запроса
        userform = NewServices()
        return render(request, "form.html", {"form": userform})


def updateServices(request):
    if request.method == "POST":  # обработка POST запроса
        userform = UpdateServices(request.POST)
        values = get_values(userform)  # данные из формы
        return HttpResponse(values)
    else:  # обработка GET запроса
        userform = UpdateServices()
        return render(request, "form.html", {"form": userform})


def searchServices(request):
    if request.method == "POST":  # обработка POST запроса
        userform = SearchServices(request.POST)
        values = get_values(userform)  # данные из формы
        return HttpResponse(values)
    else:  # обработка GET запроса
        userform = SearchServices()
        return render(request, "form.html", {"form": userform})