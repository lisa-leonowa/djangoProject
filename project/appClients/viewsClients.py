from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render
from appClients.formsClients import NewClients, UpdateClients, SearchClients
from appClients.Clients import get_values


def newClients(request):  # добавление нового клиента
    if request.method == "POST":  # обработка POST запроса
        userform = NewClients(request.POST)
        values = get_values(userform)  # данные из формы
        return HttpResponse(values)
    else:  # обработка GET запроса
        userform = NewClients()
        return render(request, "form.html", {"form": userform})


def updateClients(request):  # обновление информации о клиенте
    if request.method == "POST":  # обработка POST запроса
        userform = UpdateClients(request.POST)
        values = get_values(userform)  # данные из формы
        return HttpResponse(values)
    else:  # обработка GET запроса
        userform = UpdateClients()
        return render(request, "form.html", {"form": userform})


def searchClients(request):
    if request.method == "POST":  # обработка POST запроса
        userform = SearchClients(request.POST)
        values = get_values(userform)  # данные из формы
        return HttpResponse(values)
    else:  # обработка GET запроса
        userform = SearchClients()
        return render(request, "form.html", {"form": userform})
