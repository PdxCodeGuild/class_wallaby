import calendar

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.forms import ModelForm, DateInput
from .models import Event
from .models import *
from .utils import Calendar
from .forms import EventForm
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import DiarySerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def diary_list(request, format=None):
    """
    Get a list of products or create a product .
    """
    if request.method == 'GET':
        products = Diary.objects.all()
        serializer = DiarySerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')

def record(request):
    return render(request, 'record.html' )

def delete(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect ('calendar')


