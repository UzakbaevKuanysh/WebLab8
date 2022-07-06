from django import views
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets,generics
from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet_detail(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer

class CategoryViewSet_detail(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductsByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
       """
       This view should return a list of all the purchases for
       the user as determined by the username portion of the URL.
       """
       category_id = self.kwargs['id']
       return Product.objects.filter(category=category_id)


    
    
   