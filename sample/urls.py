from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('staff/', views.staff_list, name='staff_list'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staff/update/<int:pk>/', views.staff_update, name='staff_update'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),

    path('buyers/', views.buyer_list, name='buyer_list'),
    path('buyers/create/', views.buyer_create, name='buyer_create'),
    path('buyers/<int:pk>/', views.buyer_detail, name='buyer_detail'),
    path('buyers/update/<int:pk>/', views.buyer_update, name='buyer_update'),
    path('buyers/delete/<int:pk>/', views.buyer_delete, name='buyer_delete'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('brands/', views.brand_list, name='brand_list'),
    path('brands/create/', views.brand_create, name='brand_create'),
    path('brands/update/<int:pk>/', views.brand_update, name='brand_update'),
    path('brands/delete/<int:pk>/', views.brand_delete, name='brand_delete'),

    path('gg/', views.gg_list, name='gg_list'),
    path('gg/create/', views.gg_create, name='gg_create'),
    path('gg/update/<int:pk>/', views.gg_update, name='gg_update'),
    path('gg/delete/<int:pk>/', views.gg_delete, name='gg_delete'),

    path('challenges-in/', views.challengein_list, name='challengein_list'),
    path('challenges-in/create/', views.challengein_create, name='challengein_create'),
    path('challenges-in/update/<int:pk>/', views.challengein_update, name='challengein_update'),
    path('challenges-in/delete/<int:pk>/', views.challengein_delete, name='challengein_delete'),

    path('samples/', views.sample_list, name='sample_list'),
    path('samples/export/pdf/', views.sample_export_pdf, name='sample_export_pdf'),
    path('samples/export/excel/', views.sample_export_excel, name='sample_export_excel'),
    path('samples/<int:pk>/', views.sample_detail, name='sample_detail'),
    path('samples/create/', views.sample_create, name='sample_create'),
    path('samples/update/<int:pk>/', views.sample_update, name='sample_update'),
    path('samples/delete/<int:pk>/', views.sample_delete, name='sample_delete'),
]
