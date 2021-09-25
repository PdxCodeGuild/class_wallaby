from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question

def home(request):
    return render(request, 'pages/home.html', )

def poll(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'pages/poll.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pages/detail.html', {'question': question})

def results(request, question_id):
  return HttpResponse('results page')

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
