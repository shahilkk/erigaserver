from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,"web/home.html")


def servicesingle(request):
    return render(request,"web/servicesingle.html")


def productsingle(request):
    return render(request,"web/productsingle.html")

def contact(request):
    return render(request,"web/contact.html")

def about(request):
    return render(request,"web/about.html")

def wishlist(request):
    return render(request,"web/wishlist.html")

def checkout(request):
    return render(request,"web/checkout.html")
