from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def poll(request):
  return render(request, 'pages/poll.html')
