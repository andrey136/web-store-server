from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets          # add this
from .serializers import ProductSerializer      # add this
from .models import Product                     # add this

class ProductView(viewsets.ModelViewSet):       # add this
  serializer_class = ProductSerializer          # add this
  queryset = Product.objects.all()