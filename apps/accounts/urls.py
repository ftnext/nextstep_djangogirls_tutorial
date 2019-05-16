from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(next_page='blog:post_list'),
         name='logout'),
    path('register/', views.Register.as_view(), name='register'),
]
