from .views import BlogsList, UserCreate, LoginView, BlogDetail, BlogCreate
from django.urls import path, include
from knox import views as knox_views
urlpatterns = [
  path('blogs/', BlogsList.as_view(), name='blog_list'),
  path('blog', BlogCreate.as_view(), name='blog_create'),
  path('blogs/<int:blog_id>', BlogDetail.as_view(), name='blog_detail' ),
  path('user', UserCreate.as_view(), name='user_create'),
  path('login', LoginView.as_view(), name='login_view'),
  path('logout', knox_views.LogoutView.as_view(), name='logout_view'),
  path('auth', include('knox.urls')),
]