from django.shortcuts import render
from rest_framework import generics, response, status, permissions
from .serializers import BlogSerializer, UserSerializer
from .models import Blog
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView

class BlogListCreate(generics.ListCreateAPIView):
  permission_classes = ()
  queryset = ''
  def get(self, request, *args, **kwargs):
    print(self.kwargs, request.user, request.auth)
    if request.user.is_authenticated:
      blogs = Blog.objects.filter(created_by=request.user)
      data = BlogSerializer(blogs, many=True).data
      return response.Response(data)
    else:
      return response.Response({'error': True, 'msg': 'Not signed in.'})
  
  serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveDestroyAPIView):
  permission_classes = ()
  queryset = ''
  serializer_class = BlogSerializer
  def get(self, request, blog_id):
    if request.user.is_authenticated:
      blog = Blog.objects.get(pk=blog_id)
      data = BlogSerializer(blog).data
      return response.Response(data)
    else:
      return response.Response({'error': True, 'msg': 'Not signed in.'})


class UserCreate(generics.CreateAPIView):
  permission_classes = ()
  authentication_classes = ()
  serializer_class = UserSerializer

class LoginView(APIView):
  permission_classes = ()
  def post(self, request,):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      return response.Response({"token": user.auth_token.key})
    else: 
      return response.Response({'error': True}, status=status.HTTP_400_BAD_REQUEST)