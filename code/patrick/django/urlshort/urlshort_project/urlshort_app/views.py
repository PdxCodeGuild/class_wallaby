from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Short
from django.views.generic.edit import CreateView, DeleteView, UpdateView   
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy, reverse

from django.utils import timezone
from .forms import ShortModelForm


def home(request):
    return render(request, 'urlshort_app/home.html', {'title': 'About'})

def code_redirect(request, code):
    
   
    print(code)
    try: 
        url = Short.objects.values('url').get(pk=code) 
        print(url)
        url = url.get('url')
        print(url)
        return redirect (url)
    except:
        raise Http404
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

    def get_success_url(self):
        print(self)
        return reverse('short-detail', kwargs={'pk': self.object.pk})
        
     
class ShortUpdateView(UpdateView):
    model = Short
    fields = ['__all__']

class ShortDeleteView(DeleteView):
    model = Short
    fields = ['__all__']




