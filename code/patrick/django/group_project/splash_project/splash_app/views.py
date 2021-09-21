

from django.shortcuts import get_object_or_404, render, redirect
from .forms import ImageModel
from .key import key
import requests
from PIL import Image
import io 
from django.views.generic import ListView
import os
from .models import ProfileModel, ImageModel, Order, Item
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import datetime
from datetime import date
import random
import string



def home(request):
    
        search_term = request.POST['query1']
   
        image = f'https://api.unsplash.com/search/photos?page=1&per_page&query={search_term}&client_id={key}'
        response = requests.get(image).json()
        print(response)
        sku = response['results'][1]['id']
        photographer = response['results'][1]['user']['username']
        width = response['results'][1]['width']
        height = response['results'][1]['height']
        color = response['results'][1]['color']
        description = response['results'][1]['description']
        raw = response['results'][1]['urls']['raw']
        full = response['results'][1]['urls']['full']
        small = response['results'][1]['urls']['small']
        regular = response['results'][1]['urls']['regular']
        download = response['results'][1]['links']['download']
        thumb = response['results'][1]['urls']['thumb']
        alt_description = response['results'][1]['alt_description']
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
            sku=sku,
        )
        data.save()
        context = {
        'thumb' : response['results'][1]['urls']['thumb'],
        'alt_description': response['results'][1]['alt_description'], 
        'sku': response['results'][1]['id'], 'data': data
        }
        return render(request, 'splash_app/home.html', context = context)




def image_detail(request, id):
    img_detail = ImageModel.objects.get(id =id)
    context = {}
    return render(request, 'splash_app/detail.html', {'img_detail': img_detail})
    

def download(id):
    obj = ImageModel.objects.first(id)
    url = getattr(obj, 'download')
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'img{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)


class ProfileDetailView(ListView):
    model = ProfileModel
    queryset = ProfileModel.objects.all()
    template_name = 'splash_app/profile.html'
    context_object_name = 'profile'

def user_orders(request):
    user1 = request.user.id
    user = ProfileModel.objects.get(user_id=user1)
    
    orders = Order.objects.filter(profile=user.id)
    print(orders)
    for x in orders:
        print(x.ref_num)
       
    return render (request, 'splash_app/user_orders.html', {'orders': orders})

@login_required()
def add_cart(request, id, **kwargs):
  
    user_profile = get_object_or_404(ProfileModel, user=request.user)
    
  
    
    if id in request.user.profile.orders.all():
        messages.info(request, 'You already own this')
        return redirect(reverse('splash_app.home.html')) 
    
    order_item, status = Item.objects.get_or_create(image_id=id)
    
    user_order, status = Order.objects.get_or_create(profile=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        
        user_order.ref_num = generate_order_id()
        user_order.save()

   
    messages.success(request, "item added to cart")
    return redirect(reverse('home'))

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str