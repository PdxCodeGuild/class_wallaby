

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
from .forms import search_form



def home(request):
    
          
    contexts =[]
    search_term = request.POST.get('search')
    print(search_term)
    count = 1
    while True:
        image = f'https://api.unsplash.com/search/photos?page=1&per_page&query={search_term}&client_id={key}'
        response = requests.get(image).json()
        
        if count >= 4:
            break
        else:
            sku = response['results'][count]['id']
            photographer = response['results'][count]['user']['username']
            width = response['results'][count]['width']
            height = response['results'][count]['height']
            color = response['results'][count]['color']
            description = response['results'][count]['description']
            raw = response['results'][count]['urls']['raw']
            full = response['results'][count]['urls']['full']
            small = response['results'][count]['urls']['small']
            regular = response['results'][count]['urls']['regular']
            download = response['results'][count]['links']['download']
            thumb = response['results'][count]['urls']['thumb']
            alt_description = response['results'][count]['alt_description']
            price = 5
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
                price=price
            )
            data.save()
            stuff = {
            'thumb' : response['results'][count]['urls']['thumb'],
            'alt_description': response['results'][count]['alt_description'], 
            'sku': response['results'][count]['id'], 'price': price, 'data': data
            }
            count += 1
            contexts.append(stuff)
           
    return render(request, 'splash_app/home.html', {'contexts': contexts})




def image_detail(request,id):
    img_detail = ImageModel.objects.get(id =id)
    context = {}
    print(img_detail)
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
    order = Order.objects.all()
    orders = Order.objects.filter(profile=user.id)
    # print(orders, 'orders')
    # items = Order.objects.filter(items=orders)
    # print(items, 'items')
    # test = Order.items.filter(profile=user.id)
    # print(test)
    # print(user, 'user')
    # orders = Order.objects.filter(profile=user.id)
    projects = Order.objects.filter(profile=user.id)
    for project in projects:
        developers = project.items.all().values()
    to_show = []
    for x in developers:
       to_show.append(x['image_id'])
    print(to_show)
    image_url=[]   
    for x in to_show:
        images = ImageModel.objects.filter(pk=x).values()    
        for image in images:
            image_url.append(image['thumb'])
    context = {
        'developers': developers,
        'orders': orders,
        'image_url': image_url, 
        'to_show': to_show
    }
    
  
    return render (request, 'splash_app/user_orders.html', {'context': context})

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

def cart_view(request):
    pass

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str