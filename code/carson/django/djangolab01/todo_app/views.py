from django.shortcuts import render, redirect
from .models import Author, Note,Todo
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer,TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Todo.objects.all()
#         serializer = TodoSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TodoSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TodoSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Todo.objects.all()
#         serializer = TodoSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TodoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet =Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer =TodoSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer =TodoSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def register_author(request):
    if request.method == 'GET':
        return render(request, 'pages/register.html')
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name,)
        return redirect('add_posts')


def add_note(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    if request.method == 'GET':
        return render(request, 'pages/add_note.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        author = request.POST['author']
        result = Author.objects.get(id=author)
        Note.objects.create(author=result, title=title,
                            text=text, pub_date=pub_date)
        return redirect('view_all')


def view_all(request):
    authors = Author.objects.all()
    return render(request, 'pages/all.html', {'authors': authors})


def post_details(request, id):
    post = Note.objects.get(id=id)
    return render(request, 'pages/post_details.html', {"post": post})


def update_post(request, id):
    if request.method == 'GET':
        return render(request, 'pages/post_details.html')
    elif request.method == 'POST':
        post = Note.objects.get(id=id)
        post.text = request.POST['edit_description']
        post.save()
        return redirect('view_all')


def delete_post(request, id):
    post = Note.objects.get(id=id)
    post.delete()
    return redirect('view_all')
