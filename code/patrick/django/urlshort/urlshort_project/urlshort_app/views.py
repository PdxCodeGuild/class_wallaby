from django.shortcuts import render, redirect 
from .models import Short
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.urls import reverse_lazy
# from urlshort_app.forms import UrlForm
# from django.views.generic import (CreateView, ListView)

def home(request):
    return render(request, 'urlshort_app/home.html', {'title': 'About'})


class ShortCreateView(CreateView):
    model = Short
    fields = ['url']

class ShortUpdateView(UpdateView):
    model = Short
    fields = ['__all__']

class ShortDeleteView(DeleteView):
    model = Short
    fields = ['__all__']


# class URLFormView(FormView):
#     model = Short
#     template_name = 'urlshort_app/form.html'
#     form_class = UrlForm
    

#     def form
    
    
# class URLFormView(CreateView):
#     model = Short
#     fields = ['code', 'url']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

