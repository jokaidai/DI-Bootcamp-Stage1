from django import forms
from .models import Film, Director

class Add_Film_Form(forms.ModelForm):

    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'})
        }


class Add_Director_Form(forms.ModelForm):

    class Meta:
        model = Director
        fields = '__all__'
      