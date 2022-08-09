from django.urls import path 
from .views import family, animal, animals

urlpatterns = [ 
    path('family/<int:family_id>', family, name='family'),
    path('animal/<int:animal_id>', animal, name='animal'),
    path('animals', animals, name='animals'),
]