from django.shortcuts import render, redirect
from .models import Film, Director
from .forms import Add_Director_Form, Add_Film_Form

context = {'films': Film.objects.all(), 'directors': Director.objects.all()}

def homepage(request):
    return render( request, 'homepage.html', context)


def add_film(request):

    context.update({'forms': Add_Film_Form})
    if request.method == 'POST':
        form_filled = Add_Film_Form(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print(form_filled.errors)
    return render(request, 'film/add_film.html', context)


def add_director(request):

    context.update({'forms': Add_Director_Form})
    if request.method == 'POST':
        form_filled = Add_Director_Form(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print(form_filled.errors)
    return render(request, 'director/add_director.html', context)