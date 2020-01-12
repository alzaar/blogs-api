from .views import BlogListCreate, UserCreate, LoginView, BlogDetail
from django.urls import path

urlpatterns = [
  path('blogs/', BlogListCreate.as_view(), name='blog_list_create'),
  path('blogs/<int:blog_id>/', BlogDetail.as_view(), name='blog_detail' ),
  path('user/', UserCreate.as_view(), name='user_create'),
  path('login/', LoginView.as_view(), name='login_view')
]