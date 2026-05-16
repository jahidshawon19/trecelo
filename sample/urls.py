from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('staff/', views.staff_list, name='staff_list'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/update/<int:pk>/', views.staff_update, name='staff_update'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),

    path('buyers/', views.buyer_list, name='buyer_list'),
    path('buyers/create/', views.buyer_create, name='buyer_create'),
    path('buyers/update/<int:pk>/', views.buyer_update, name='buyer_update'),
    path('buyers/delete/<int:pk>/', views.buyer_delete, name='buyer_delete'),

    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
]
