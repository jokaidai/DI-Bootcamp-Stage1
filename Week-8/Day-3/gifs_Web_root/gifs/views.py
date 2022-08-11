from http.client import HTTPResponse
from django.shortcuts import render
from .models import Category, Gif
from .forms import GifForms, CategoryForm

# Create your views here.

def homepage(request) -> HTTPResponse: 

    context = {
        # 'categories' : Category.objects.all(),
        'gifs' : Gif.objects.all()
    }

    return render(request, 'homepage.html', context)


def add_new_gif(request) -> HTTPResponse:

    if request.method == 'POST':

        form_filled = GifForms(request.POST)
        if form_filled.is_valid():
            title = form_filled.cleaned_data['title']
            uploader_name = form_filled.cleaned_data['uploader_name']
            url = form_filled.cleaned_data['url']
            categories  = form_filled.cleaned_data['categories']

            new_gif = Gif(title = title, uploader_name = uploader_name, url = url)
            new_gif.save()

        for category in categories:
            new_gif.categories.add(category)
        new_gif.save()
           

    context = {'form': GifForms}
    return render(request, 'add_new_gif.html', context)


def add_new_category(request) -> HTTPResponse:

    if request.method == 'POST':
    
        form_filled = CategoryForm(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']

            Category.objects.create(name = name) 

    context = {'form': CategoryForm}
    return render(request, 'add_new_category.html', context)


def show_category(request, id) -> HTTPResponse:
    
    category = Category.objects.get(id = id)
    gifs = category.gif.all()

    context = {
        'category': category,
        'gifs': gifs
    }

    return render(request, 'show_category.html', context)



def show_categories(request) -> HTTPResponse:
    
    categories = Category.objects.all()
 

    context = {
        'categories': categories,
    }

    return render(request, 'show_categories.html', context)