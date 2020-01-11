from .views import BlogViewSet, UserCreate, LoginView
from django.urls import path

urlpatterns = [
  path('blogs/', BlogViewSet.as_view(), name='blog_viewset'),
  path('user/', UserCreate.as_view(), name='user_create'),
  path('login/', LoginView.as_view(), name='login_view')
]