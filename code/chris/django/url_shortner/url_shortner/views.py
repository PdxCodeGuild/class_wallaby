from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from url_shortner.models import Url

# Create your views here.
def root(request):
  return render(request, 'pages/root.html')

def surl_parse(request, surl):
  l = Url.objects.filter(surl=surl)
  print(l[0])
  return redirect(f'{l[0]}')
