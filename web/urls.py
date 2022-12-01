from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('',views.home,name='home'),
    path('servicesingle',views.servicesingle,name='servicesingle'),
    path('productsingle',views.productsingle,name='productsingle'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('checkout',views.checkout,name='checkout'),
    # path('about',views.about,name='about'),

]
   