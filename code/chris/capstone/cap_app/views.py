from django.core.checks.messages import Error
from django.shortcuts import render, HttpResponse, redirect
from cap_app.models import *
import datetime
from django.utils import timezone


def index(request):
    g = Gestures.objects.all().values()
    # print(g)
    gesture = None
    next = None
    timeoutMsg = "4 months"
    print('index running')


    for gesture in g:
        if gesture['bin'] == 2:
            minutes = 3
            timeoutMsg = f'{minutes} minutes'
            if gesture['dateCorrect'] + datetime.timedelta( minutes=minutes ) < timezone.now():
                next = gesture
                break
        if gesture['bin'] == 1:
            minutes = 1
            timeoutMsg = f'{minutes} minute'
            if gesture['dateCorrect'] + datetime.timedelta( minutes=minutes ) < timezone.now():
                next = gesture
                break
        elif gesture['bin'] == 0:
            next = gesture
            break



    context = {
        'gestures': g,
        'gesture': next,
        'timeoutMsg': timeoutMsg
    }
    return render(request, 'pages/home.html', context)

def admin(request):
    return render(request, 'pages/admin.html')

def profile(request):
    return render(request, 'pages/profile.html')

def answer(request, answer_id):
    g = Gestures.objects.get(id=answer_id)
    g.timesCorrect += 1
    g.bin += 1
    g.save()
    return redirect('index')

def wrong(request, answer_id):
    g = Gestures.objects.get(id=answer_id)
    g.timesIncorrect += 1
    g.bin = 0
    g.save()
    return redirect('index')

def stats(request):
    g = Gestures.objects.all().values()
    context = {
        'g': g,
    }
    return render(request, 'pages/stats.html', context)


def reset(request):
    try:
        Gestures.objects.all().delete()
        Gestures.objects.create(id = 1, name = 'A', imgURL='A.png')
        # Gestures.objects.create(id = 2, name = 'B', imgURL='B.svg')
        Gestures.objects.create(id = 3, name = 'C', imgURL='C.svg')
        # Gestures.objects.create(id = 4, name = 'L', imgURL='L.svg')
        Gestures.objects.create(id = 5, name = 'Y', imgURL='Y.svg')
    except:
        print('Error')
    finally:
        return HttpResponse(Gestures.objects.all().values())

def testPOST(request):
    print('test post contacted')

