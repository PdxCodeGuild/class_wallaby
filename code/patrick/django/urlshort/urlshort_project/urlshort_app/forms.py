from django import forms
from .models import Short

class ShortModelForm(forms.ModelForm):
    class Meta:
        model = Short
        fields = [
            'url'

        ]
    
    