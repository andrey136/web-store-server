from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework import viewsets          # add this
from .serializers import ProductSerializer      # add this
from .models import Product                     # add this

class ProductView(viewsets.ModelViewSet):       # add this
  serializer_class = ProductSerializer          # add this
  queryset = Product.objects.all()

def home_view(request, *args, **kwargs):
#   return HttpResponse("<h1>Hello World</h1>")
  print(request)
  return render(request, 'home.html', {})
  

def get_img_view(*args, **kwargs):
  return HttpResponse("""<img src="img/fridge.jpg">Fridge</img>""")