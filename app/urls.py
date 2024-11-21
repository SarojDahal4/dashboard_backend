from itertools import product
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ('customer_add/', views.customerList, name='Customer'),
    path ('customer_lists/', views.Customer_lists, name='Customer_List'),
    path ('customer/<int:id>/',views.customer, name='customer_list'),
    path ('customer_update/<int:id>/',views.customer_update, name='customer_update'),
    path ('customer_delete/<int:id>/', views.customer_delete, name='customer_delete'),
    
    
    
    path ('product_add/', views.product_add, name='Product'),
    path ('product_lists/', views.product_lists, name="product_list"),
    path ('product/<int:id>/', views.product,name='product_list'),
    path ('product_update/<int:id>/', views.Product_update, name='product_update'),
    path ('product_delete/<int:id>/', views.product_delete, name='product_delete'),
    
]