# from django.http.response import JsonResponse

# from django.contrib import messages

# from rest_framework.parsers import JSONParser
# from info_app.serializers import UserSerializer

# from users.serializers import user_image_serializer


# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})



# def profile(request):
    
        # u_form = UserUpdateForm(request.POST, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST,
        #                            request.FILES,
        #                            instance=request.user.profile)
        # if u_form.is_valid() and p_form.is_valid():
        #     u_form.save()
        #     p_form.save()
        #     messages.success(request, f'Your account has been updated!')
        #     return redirect('profile')
        # data = JSONParser().parse(request)
        # print(data, ' data')
        # serializer = UserSerializer(data=data
        #                            )
        # print(serializer)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)

   
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import user_image_serializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from users import serializers
# Create your views here.


@permission_classes([IsAuthenticated])
class ProfileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    

    def get(self, request, *args, **kwargs):
        context={'request': request}
       
        profiles = Profile.objects.all()
        serializer = user_image_serializer(profiles, many=True, context=context)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        context={'request': request}
        posts_serializer = user_image_serializer(data=request.data, context=context)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    
