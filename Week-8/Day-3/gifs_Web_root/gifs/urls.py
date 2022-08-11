from django.urls import path
from .views import (
    homepage, 
    add_new_gif, 
    add_new_category,
    show_category,
    show_categories
    )

urlpatterns = [
    path("homepage", homepage, name="homepage"),
    path("add_new_gif", add_new_gif, name="add_new_gif"),
    path("add_new_category", add_new_category, name="add_new_category"),
    path("show_category/<int:id>", show_category, name="show_category"),
    path("show_categories", show_categories, name="show_categories"),

]