from django import forms
from .models import Category


class GifForms(forms.Form):

    uploader_name = forms.CharField(max_length = 50)
    title = forms.CharField(max_length = 50)
    url = forms.URLField()
    categories = forms.ModelMultipleChoiceField(queryset = Category.objects.all())


class CategoryForm(forms.Form):

    name = forms.CharField(max_length = 50)



