from django.http import HttpResponse
from django.shortcuts import render # библиотека для обработки запросов
from .formsServices import NewServices, UpdateServices, SearchServices


def newSevices(request):
    if request.method == "POST":
        pass
    else:
        userform = NewServices()
        return render(request, "form.html", {"form": userform})


def updateServices(request):
    if request.method == "POST":
        pass
    else:
        userform = UpdateServices()
        return render(request, "form.html", {"form": userform})


def searchServices(request):
    if request.method == "POST":
        pass
    else:
        userform = SearchServices()
        return render(request, "form.html", {"form": userform})