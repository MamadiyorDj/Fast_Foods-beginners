from .views import *
from django.urls import path

urlpatterns = [
#    path('', register, name='register')
    path('', CategoryListView.as_view(), name='categories_list'),
    path('<int:id>/', category, name='category'),
#    path('/<int:id>', CategoryDetailView.as_view(), name='category')
    path('products/', ProductListView.as_view(), name='products_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product'),
]
