from calendar import c
import email
from sre_parse import CATEGORIES
from unicodedata import category
from django.http import HttpResponse, HttpResponseGone
from django.shortcuts import render , redirect
from matplotlib.style import context
from numpy import product
from .models import Product , Category ,Customer

# Create your views here.
def index(request):
    product = None
    CATEGORIES = Category.get_all_Category()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.get_all_product_by_id(categoryID)
    else:
        product = Product.get_all_products()

    context = {
        'products' : product,
        'categories': CATEGORIES
    }
    
    # return render(request,template_name='orders/order.html',context=context)
    return render(request,template_name='index.html',context=context)

def signup(request):
    if request.method == 'GET':
        return render(request,template_name='signup.html')
    else:
        postData = request.POST
        Name = postData.get('name')
        Phone = postData.get('phone')
        Email = postData.get('email')
        Password = postData.get('password')
        print(Name , Phone , Email , Password)

        customer = Customer(name = Name,phone = Phone , email = Email , password=Password)

        if customer.isExists():
            error_message = 'Email Address Alredy Register..'
            print(error_message)
            return render(request,template_name='signup' )
        else:
            customer.register()
            return redirect('homepage')