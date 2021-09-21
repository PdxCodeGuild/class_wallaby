from django.shortcuts import get_object_or_404, render, redirect
import os
import io 
import shutil
# from .forms import ImageModel
# import requests
# from PIL import Image

# from django.views.generic import DetailView

# from .models import ProfileModel, ImageModel, Order, Item
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.urls import reverse
# import datetime
# from datetime import date
# import random
# import string

def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
def cart(request):
    return render(request, 'cart.html')

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

# def home(request):
    # image = f'https://api.unsplash.com/photos/random/?client_id=oipa2QJFQiBFEcO4MMvho2qH_kIrvBl72vM8_y7g538'
    # response = requests.get(image).json()
    # photographer = response['user']['username']
    # width = response['width']
    # height = response['height']
    # color = response['color']
    # description = response['description']
    # raw = response['urls']['raw']
    # full = response['urls']['full']
    # small = response['urls']['small']
    # regular = response['urls']['regular']
    # download = response['links']['download']
    # thumb = response['urls']['thumb']
    # alt_description = response['alt_description']
    # id = response['id']
    # data = ImageModel(
    #     photographer=photographer,
    #     width = width, 
    #     height = height, 
    #     color = color, 
    #     description = description,
    #     raw=raw,
    #     full=full, 
    #     small=small,
    #     regular=regular, 
    #     download=download, 
    #     thumb=thumb, 
    #     alt_description=alt_description,
    #     id=id,
    # )
    # data.save()
    # context = {
    #  'thumb' : response['urls']['thumb'],
    #  'alt_description': response['alt_description'], 
    #  'id': response['id']
    #  }
    # print(context)
    # return render(request, 'splash_app/home.html') #context = context) 

# def image_detail(request, id):
#     image = f'https://api.unsplash.com/photos/:{id}/?client_id={key}'
#     response = requests.get(image).json()
#     context = {'thumb' : response['urls']['thumb'], 'alt_description': response['alt_description']}
    
#     return render(request, 'splash_app/detail.html', context = context) 

# def image_detail(request, id):
    
#     context = {}
#     context['data'] = ImageModel.objects.get(id =id)
#     return render(request, 'splash_app/detail.html', context)

# def download(id):
#     obj = ImageModel.objects.first(id)
#     url = getattr(obj, 'download')
#     page = requests.get(url)

#     f_ext = os.path.splitext(url)[-1]
#     f_name = 'img{}'.format(f_ext)
#     with open(f_name, 'wb') as f:
#         f.write(page.content)





        # r = ImageModel.objects.get(download='download', stream=True)
        # if r.status_code == 200:
        #     r.raw.decode_content = True
        #     with open(filename,'wb') as f:
        #         shutil.copyfileobj(r.raw, f)
    
# def image_detail(request, id):       
#     context = {}
#     context['data'] = ImageModel.objects.get(id =id)
#     return render(request, 'splash_app/detail.html', context)

# class ProfileDetailView(DetailView):
#     model = ProfileModel
#     queryset = ProfileModel.objects.all()
#     template_name = 'profile.html'


# @login_required
# def add_cart(request, **kwargs):
#     user = get_object_or_404(ProfileModel, user=request.user)
#     product = ImageModel.objects.filter(id=kwargs.get('id', '')).first()
#     order_item, status = Item.objects.get_or_create(image=product)
#     user_order, status = Order.objects.get_or_create(profile=user,  is_ordered=False)
#     user_order.items.add(order_item)
#     if status:
#         # generate a reference code
#         user_order.ref_code = generate_order_id()
#         user_order.save()
#     messages.info(request, "item added to cart")
#     return redirect(reverse('home'))

# def generate_order_id():
#     date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
#     rand_str = "".join([random.choice(string.digits) for count in range(3)])
#     return date_str + rand_str