from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('user/', views.user, name='user'),
    path('logout/', views.logout, name='logout'),
]
