from django.contrib import admin
from .models import Category, Country

admin.site.register(Country)
admin.site.register(Category)