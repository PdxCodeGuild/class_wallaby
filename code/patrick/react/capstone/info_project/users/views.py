from django.views import generic
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UpdateUserSerializer, user_image_serializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User


@permission_classes([IsAuthenticated])
class ProfileView(APIView): 
    def patch(self, request):
        context={'request': request}
        profile_serializer = user_image_serializer(request.user.userprofile, data=request.data, context=context, partial=True)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', profile_serializer.errors)
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@permission_classes([IsAuthenticated])
class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer


