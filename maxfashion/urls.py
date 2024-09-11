from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="home"),
    path("fashion",views.fashion,name="fashion"),
    path("electronic",views.electronic,name="electronic"),
    path("jewellery",views.jewellery,name="jewellery"),
    path("store",views.store,name="store"), 
    path("checkout",views.checkout,name="checkout"),    
    path("cart/<int:id>",views.cart,name="cart"),   
]