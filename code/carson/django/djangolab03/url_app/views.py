from url_app.models import URL_shorten
from django.shortcuts import render
from django.utils.crypto import get_random_string


from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def shorten_url(request):
    url = URL_shorten.objects.all()
 
    i = {
            "url": url
        }
    if request.method == 'GET':
        return render(request, 'shorten.html', i)
    
    elif request.method == 'POST':
        input_url = request.POST['url'] 
        split_url = input_url.split('/')
        random_text = get_random_string(length=7) 
        finished_url = split_url[0] +  '/' + random_text
        complete = URL_shorten.objects.create(original = input_url, updated = finished_url)
        return render(request, 'shorten.html', i)


  