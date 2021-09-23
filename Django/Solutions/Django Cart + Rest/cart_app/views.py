from django.shortcuts import render
from .models import Cart, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#--> Rest
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import ProductSerializer, CartSerializer, UserSerializer 
from rest_framework.response import Response
#-->

@api_view(['GET'])
def get_user(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def retrieve_cart(request, pk):
    try:
        cart = Cart.objects.get(user=pk)
        products = Product.objects.filter(session=cart)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(products,  many=True)
        return Response(serializer.data)




# @login_required
@api_view(['GET', 'POST'])
def product_list(request, format=None):
    """
    Get a list of products or create a product .
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##PUT request to update the status of an existing product
## request links the product to the cart of logged person
# @login_required
@api_view(['PUT'])
def add_cart(request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk, format=None):
    """
    Retrieve, update or delete a product by id.
    """
    try:
        products = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@login_required
def home(request):
    products = Product.objects.all()
    user = request.user
    user_cart = Cart.objects.get_or_create(user=user)
    cart_session = Cart.objects.get(user=user.id)
    context = {
      "products": products,
      "cart_session": cart_session.id,
    }
    print(user_cart, cart_session)
    return render(request, 'home.html', context)

@login_required
def get_cart(request):
    user = request.user.id
    cart_session = Cart.objects.filter(user=request.user).first()
    order = Product.objects.filter(session=cart_session)
    total = 0
    for x in order:
        total += sum([x.price * x.quantity])
    context = {
        'order': order,
        'total': total,
         'user': user
    }
    return render(request, 'cart.html', context)

# @api_view(['PUT'])
# def update_cart(request, pk):
#     try:
#         products = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProductSerializer(products, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##function to update product.
##makes a PUT request and subtracts the quantity added in the text field from the overall product quantity
##if amount goes below 0, return erorr message