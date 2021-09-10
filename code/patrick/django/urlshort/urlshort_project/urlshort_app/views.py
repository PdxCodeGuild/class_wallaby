from django.shortcuts import get_object_or_404, render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Short
from django.views.generic.edit import CreateView, DeleteView, UpdateView   
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .forms import ShortModelForm
from django.utils.crypto import get_random_string


def home(request):
    return render(request, 'urlshort_app/home.html', {'title': 'About'})

class URLDetailView(DetailView):
    queryset = Short.objects.all()

class ShortListView(ListView):
    model = Short
    template_name = 'urlshort_app/short_list.html'
    context_object_name = 'urls'
    queryset = Short.objects.all() # <app>/<modelname>_list.html

class ShortDetailView(DetailView):
    model = Short
    template_name = 'urlshort_app/short_detail.html'
    context_object_name = 'urls'
    queryset = Short.objects.all() # <app>/<modelname>_list.html

   
class ShortCreateView(CreateView):
    model = Short
    form_class =  ShortModelForm
    queryset = Short.objects.all()


    

  
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
