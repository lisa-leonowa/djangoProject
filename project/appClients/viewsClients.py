from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from project.appClients.formsClients import NewClients, UpdateClients, SearchClients


def newClients(request):
    if request.method == "POST":
        return HttpResponsePermanentRedirect("/")
    else:
        userform = NewClients()
        return render(request, "form.html", {"form": userform})


def updateClients(request):
    if request.method == "POST":
        return HttpResponsePermanentRedirect("/")
    else:
        userform = UpdateClients()
        return render(request, "form.html", {"form": userform})


def searchClients(request):
    if request.method == "POST":
        return HttpResponsePermanentRedirect("/")
    else:
        userform = SearchClients()
        return render(request, "form.html", {"form": userform})
