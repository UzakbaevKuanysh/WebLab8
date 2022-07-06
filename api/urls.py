from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryViewSet, CategoryViewSet_detail, ProductViewSet, ProductViewSet_detail, ProductsByCategory
products = ProductViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
products_detail = ProductViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

categories = CategoryViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
category_detail = CategoryViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

urlpatterns = [
    path('products/', products, name = 'products'),
    path('products/<int:pk>', products_detail, name = "products_detail"),
    path('categories/', categories, name = 'categories'),
    path('categories/<int:pk>', category_detail, name = "category_detail"),
    path('categories/<int:id>/products', ProductsByCategory.as_view(), name = "category_products")
]
urlpatterns = format_suffix_patterns(urlpatterns)
