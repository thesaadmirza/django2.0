from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForms
# Create your views here.



def index(request):
    products = Product.objects.all()

    return render(request,'dashboard.html',{'products':products})

def editProduct(request,id):
    product  = Product.objects.get(id=id)
    form = ProductForms()
    return render(request,'viewproduct.html',{'product':product,'form':form})


def deleteProduct(request):
    return HttpResponse("hey this is deleting controller")
def updateProduct(request):
    return HttpResponse('hey')