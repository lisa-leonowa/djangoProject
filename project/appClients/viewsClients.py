from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render
from appClients.formsClients import NewClients, UpdateClients, SearchClients
from appClients.Clients import get_values, add_client, update_client, select_clients


def newClients(request):  # добавление нового клиента
    if request.method == "POST":  # обработка POST запроса
        userform = NewClients(request.POST)
        values = get_values(userform)  # данные из формы
        if add_client(values):
            return HttpResponse("Клиент добавлен")
        else:
            return HttpResponse("Клиент не был добавлен (возможно он уже существует)")
    else:  # обработка GET запроса
        userform = NewClients()
        return render(request, "form.html", {"form": userform})

def index(request):  # добавление нового клиента
    context = {}
    context['clients'] = select_clients()
    return render(request, "index.html", context=context)

def updateClients(request):  # обновление информации о клиенте
    if request.method == "POST":  # обработка POST запроса
        userform = UpdateClients(request.POST)
        values = get_values(userform)  # данные из формы
        if update_client(values):
            return HttpResponse("Информация о клиенте была обновлена")
        else:
            return HttpResponse("Не удалось обновить информаицию о клиенте (возможно информации о нем нет в базе)")
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
