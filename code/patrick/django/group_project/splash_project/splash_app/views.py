from django.shortcuts import render
from .forms import ImageModel
from .key import key
import requests
from PIL import Image
import io 
from django.views.generic import DetailView


# def home(request):
#     if request == 'GET':
        
       
#         photographer = response['user']['username']
#         width = response['width']
#         height = response['height']
#         color = response['color']
#         description = response['description']
        
#         raw = response['urls']['raw']
#         full = response['urls']['full']
#         small = response['urls']['small']
        
#         regular = response['urls']['regular']
#         download = response['links']['download']
#         return(id, width, height, color, description, alt_description, raw, full, small, thumb, regular, download)
#     elif request == 'GET':
#         pass

def home(request):
    image = f'https://api.unsplash.com/photos/random/?client_id={key}'
    response = requests.get(image).json()
    context = {
     'thumb' : response['urls']['thumb'],
     'alt_description': response['alt_description'], 
     'id': response['id']
     
     }
    print(context)
    return render(request, 'splash_app/home.html', context = context)

def image_detail(request, id):
    image = f'https://api.unsplash.com/photos/:{id}/?client_id={key}'
    response = requests.get(image).json()
    context = {'thumb' : response['urls']['thumb'], 'alt_description': response['alt_description']}
    
    return render(request, 'splash_app/detail.html', context = context) 
