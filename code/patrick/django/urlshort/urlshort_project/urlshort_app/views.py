from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Short
from django.views.generic.edit import CreateView, DeleteView, UpdateView  
from django.views.generic import DetailView
from django.urls import reverse_lazy, reverse
from django.utils import timezone


def home(request):
    return render(request, 'urlshort_app/home.html', {'title': 'About'})

class URLDetailView(DetailView):
    queryset = Short.objects.all()

    def get_object(self):
        obj=super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


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

