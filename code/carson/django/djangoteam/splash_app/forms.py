from django import forms 
from .models import ImageModel

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title']