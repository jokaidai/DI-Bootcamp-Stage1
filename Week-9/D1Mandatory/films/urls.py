
from django.urls import path
from .views import(
    homepage,
    add_film,
    add_director
    )

urlpatterns = [
   path('homepage', homepage, name = 'homepage'),
   path('add_film', add_film, name = 'add_film'),
   path('add_director', add_director, name = 'add_director'),
]