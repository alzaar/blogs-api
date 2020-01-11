from django.shortcuts import render
from rest_framework import generics, response, status
from .serializers import BlogSerializer, UserSerializer
from .models import Blog
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView

class BlogViewSet(generics.ListCreateAPIView):
  permission_classes = ()
  def get(self, request, *args, **kwargs):
    # username = request.data.get('username')
    # password = request.data.get('password')
    # user = authenticate(username=username, password=password)
    # user_id = User.objects.get(username=user)
      # blogs = blogs.objects.filter(created_by=user_id)
    # print(user_id, 123, request.user)

    # if user:
    return response.Response(
      {
    "msg": "hello"
}
    )

  serializer_class = BlogSerializer

class UserCreate(generics.CreateAPIView):
  permission_classes = ()
  authentication_classes = ()
  serializer_class = UserSerializer

class LoginView(APIView):
  permission_classes = ()
  def post(self, request,):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      return response.Response({"token": user.auth_token.key})
    else: 
      return response.Response({'error': True}, status=status.HTTP_400_BAD_REQUEST)