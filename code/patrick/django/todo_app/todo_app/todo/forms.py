from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    title = forms.TextInput(),
    description = forms.Textarea(),
    create = forms.TextInput()
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']   

     # widgets = {
        #     'user': forms.Select(attrs={'class': 'form-control'}),
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'complete': forms.Select(attrs={'class': 'form-control'}),
        #     'create': forms.TextInput(attrs={'class': 'form-control'}),
        # } decided to not user generic views