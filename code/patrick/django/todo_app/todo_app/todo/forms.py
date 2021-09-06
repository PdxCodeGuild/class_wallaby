from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

    

     # widgets = {
        #     'user': forms.Select(attrs={'class': 'form-control'}),
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'complete': forms.Select(attrs={'class': 'form-control'}),
        #     'create': forms.TextInput(attrs={'class': 'form-control'}),
        # } decided to not user generic views