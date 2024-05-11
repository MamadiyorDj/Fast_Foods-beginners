from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UsersListAPIView.as_view(), name='users_list'),
    path('users/update/<int:pk>/', UsersRetrieveUpdateDestroyAPIView.as_view(), name='users_get_put_delete'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_get_put_delete'),
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_get_put_delete'),
    path('users/', UsersListAPIView.as_view(), name='users_list'),
    path('fastfoods/', FastFoodsListAPIView.as_view(), name='fastfood_list'),
    path('fastfood/<int:pk>/', FastFoodDetailAPIView.as_view(), name='fastfood_detail'),
    path('fastfood/create/', FastFoodCreateAPIView.as_view(), name='fastfood_create'),
    path('fastfood/update/<int:pk>/', FastfoodRetrieveUpdateDestroyAPIView.as_view(), name='fastfood_get_put_delete'),
    path('orders/', OrdersListAPIView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDetailAPIView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order_create'),
    path('order/update/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order_get_put_delete'),
    path('order_items/', OrderItemsListAPIView.as_view(), name='order_items_list'),
    path('order_items/<int:pk>', OrderItemDetailAPIView.as_view(), name='order_items_detail'),
    path('order_items/create/', OrderItemCreateAPIView.as_view(), name='order_items_create'),
    path('order_items/update/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='order_items_get_put_delete'),

]