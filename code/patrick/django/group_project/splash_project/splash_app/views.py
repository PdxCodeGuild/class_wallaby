

from django.shortcuts import render
import shutil
from .forms import ImageModel
from .key import key
import requests
from PIL import Image
import io 
from django.views.generic import DetailView
import os



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
    photographer = response['user']['username']
    width = response['width']
    height = response['height']
    color = response['color']
    description = response['description']
    raw = response['urls']['raw']
    full = response['urls']['full']
    small = response['urls']['small']
    regular = response['urls']['regular']
    download = response['links']['download']
    thumb = response['urls']['thumb']
    alt_description = response['alt_description']
    id = response['id']
    data = ImageModel(
        photographer=photographer,
        width = width, 
        height = height, 
        color = color, 
        description = description,
        raw=raw,
        full=full, 
        small=small,
        regular=regular, 
        download=download, 
        thumb=thumb, 
        alt_description=alt_description,
        id=id,
    )
    data.save()
    context = {
     'thumb' : response['urls']['thumb'],
     'alt_description': response['alt_description'], 
     'id': response['id']
     }
    # print(context)
    return render(request, 'splash_app/home.html', context = context)

# def image_detail(request, id):
#     image = f'https://api.unsplash.com/photos/:{id}/?client_id={key}'
#     response = requests.get(image).json()
#     context = {'thumb' : response['urls']['thumb'], 'alt_description': response['alt_description']}
    
#     return render(request, 'splash_app/detail.html', context = context) 

def image_detail(request, id):
    
    context = {}
    context['data'] = ImageModel.objects.get(id =id)
    return render(request, 'splash_app/detail.html', context)

def download(id):
    obj = ImageModel.objects.first(id)
    url = getattr(obj, 'download')
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'img{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)





        # r = ImageModel.objects.get(download='download', stream=True)
        # if r.status_code == 200:
        #     r.raw.decode_content = True
        #     with open(filename,'wb') as f:
        #         shutil.copyfileobj(r.raw, f)
    
# def image_detail(request, id):       
#     context = {}
#     context['data'] = ImageModel.objects.get(id =id)
#     return render(request, 'splash_app/detail.html', context)