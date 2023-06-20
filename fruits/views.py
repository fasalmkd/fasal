from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
def index(request):
    item=Product.objects.all()
    return render(request,"index.html",{'item':item})

# Create your views here.
