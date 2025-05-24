from django.urls import path
from .views import *
urlpatterns = [
    path('shop/',shop,name='shop'),
    path('createitem/',createitem,name='createitem'),
    path('cartview/',cartview,name='cartview'),
    path('addtocart/',addtocart,name='addtocart'),
    path('deletecart/<int:id>/',deletecart,name='deletecart'),
    path('checkout/',checkout,name='checkout'),
    
]