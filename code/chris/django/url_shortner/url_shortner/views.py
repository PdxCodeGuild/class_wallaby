from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from url_shortner.models import Url

# Create your views here.
def root(request):
  s = Url.objects.all()
  context = {
    'allUrls': s,
  }
  return render(request, 'pages/root.html', context)

def surl_parse(request, shortUrl):
  l = Url.objects.filter(surl=shortUrl).first()

  return redirect(f'{l}')


def addurl(request):
  print(50 * '_')
  print(request)
  return HttpResponse('add url page')
