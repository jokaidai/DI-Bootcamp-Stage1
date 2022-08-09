from django.shortcuts import render
from django.http import HttpResponse
from .models import Family, Animal

# Create your views here.

def family(request, family_id) -> HttpResponse:
    
    family = Family.objects.get(id = family_id)
    animals_of_family = Animal.objects.filter(family_id=family_id)
    context = {
        'family': family,
        'animals': animals_of_family
    }
    return render(request, 'family.html', context)


def animal(request, animal_id) -> HttpResponse:

    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal.html', {'animal': animal})


def animals(request) -> HttpResponse:

    animals = Animal.objects.all()
    return render (request, 'animals.html', {'animals': animals})