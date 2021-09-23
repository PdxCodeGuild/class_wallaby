from django import forms 
from .models import ImageModel

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title']

class search_form(forms.Form):
    search = forms.CharField(label='search')
    print(search, 'form output')
    value = forms.CharField(label='search')