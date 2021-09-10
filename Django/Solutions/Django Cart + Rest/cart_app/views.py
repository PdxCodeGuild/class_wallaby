from django.shortcuts import render
from .models import Cart, Product
from rest_framework import viewsets
from django.core import serializers as quickSerializer


#--> Rest
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import ProductSerializer, CartSerializer  
from rest_framework.response import Response
#-->

# class productView(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     def get_queryset(self):
#         return Product.objects.all()



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

def home(request):
    products = Product.objects.all()
    serialized_products = quickSerializer.serialize("json", Product.objects.all()) 
    print(serialized_products)
    user = request.user
    context = {
      "products": products,
      "user": user,
      "serialized_products": serialized_products
    }
    user_cart = Cart.objects.get_or_create(user=user)
    print(user_cart)

    return render(request, 'home.html', context)