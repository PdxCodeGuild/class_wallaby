from django.shortcuts import render, requests
from .key import key
import requests

def home(request):
    return render(request, 'splash_app/home.html')

def get_images():
    
    image= f'https://api.unsplash.com/photos/random/?client_id={key}'
    response = requests.get(image).json()
    return response
    
