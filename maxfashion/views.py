from django.shortcuts import render
from . models import Jewellery, Checkout
from .forms import StoreForm, CheckoutForm

def index(request):
    return render(request, "index.html")

def electronic(request):
    return render(request, "electronic.html")

def fashion(request):
    return render(request, "fashion.html")

def jewellery(request):
    item=Jewellery.objects.all()
    data ={
        "item":item,
    }
    return render(request, "jewellery.html",data)
def store(request):
    item=Jewellery.objects.all()
    form=StoreForm()
    data ={
        "item":item,
        "form":form,
    }
    if request.method=='POST':
        store=StoreForm(request.POST,request.FILES)
        if store.is_valid():
            store.save()
    return render(request, "store.html",data)
def checkout(request):
    out=Checkout.objects.all()
    form1=CheckoutForm()
    data ={
        "out":out,
        "form1":form1,
    }
    if request.method=='POST':
        checkout=CheckoutForm(request.POST,request.FILES)
        if checkout.is_valid():
            checkout.save()
    return render(request, "checkout.html",data)
def cart(request, id):
    item=Jewellery.objects.get(id=id)
    data ={
        "item":item,
    }
    return render(request, "cart.html",data)
