from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")