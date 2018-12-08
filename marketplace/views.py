from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import product, Order, OrderItem
from . import forms
from django.contrib import messages
from django.template.loader import render_to_string
import datetime
import stripe
from .extras import generate_order_id


def products_all(request):
    product_blog = product.objects.all()
    return render(request, 'marketplace/productsblog.html',{'products':product_blog})

def product_details(request, slug):
    pro_details = product.objects.get(pk=slug)
    return render(request, 'marketplace/product_details.html', {'details':pro_details})

@login_required(login_url="http://127.0.0.1:8000/register/login/")

def add_product(request):
    if request.method == "POST":
        form = forms.productform(request.POST,request.FILES)
        if form.is_valid():
            product_instance = form.save(commit=False)
            product_instance.fullname = request.user
            product_instance.save()
            return redirect('marketplace:products_blog')


    else:
        form = forms.productform()
    return render(request, 'marketplace/product_add.html',{'form':form})
@login_required(login_url="http://127.0.0.1:8000/register/login/")
def my_products(request):
    uname = request.user
    my_product = product.objects.filter(fullname = uname)
    return render(request, 'marketplace/my_products.html',{'my_pro':my_product})
@login_required(login_url="http://127.0.0.1:8000/register/login/")
def edit_product(request, id = None):
    instance= get_object_or_404(product, pk= id)
    form= forms.productform(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('marketplace:products_blog')
    context={
        'form':form,
    }
    return render(request, 'marketplace/edit_product.html',{'form':form})

@login_required(login_url="http://127.0.0.1:8000/register/login/")
def delete_product(request, id):
    instance= get_object_or_404(product, pk= id)
    instance.delete()
    return redirect('marketplace:products_blog')

def add_to_cart(request, id):
    if request.method == "POST":
        prod = product.objects.get(id=id)
        user_order, status = Order.objects.get_or_create(user=request.user, is_ordered=False)
        if status:
            ref_code = generate_order_id()
            order_item, status = OrderItem.objects.get_or_create(product=prod, ref_code=ref_code)
            user_order.items.add(order_item)
            user_order.ref_code = ref_code
            user_order.save()
        else:
            order_item, status = OrderItem.objects.get_or_create(product=prod, ref_code=user_order.ref_code)
            user_order.items.add(order_item)
            user_order.save()
        order_item.cost = order_item.qty * order_item.product.cost
        order_item.save()
        return render(request, 'marketplace/cart.html', {'order':user_order})
    else:
        prod = product.objects.get(id=id)
        user_order, status = Order.objects.get_or_create(user=request.user, is_ordered=False)
        order_item = OrderItem.objects.get(product=prod, ref_code=user_order.ref_code)
        order_item.cost = order_item.qty * order_item.product.cost
        order_item.save()
        return render(request, 'marketplace/cart.html', {'order':user_order})

def add_quantity(request, id):
    item = OrderItem.objects.get(pk=id)
    if item.qty < item.product.quantity:
        item.qty = item.qty + 1
        item.save()
    return redirect('/marketplace/add_to_cart/'+str(item.product.id))

def remove_quantity(request, id):
    item = OrderItem.objects.get(pk=id)
    item.qty = item.qty - 1
    item.save()
    return redirect('/marketplace/add_to_cart/'+str(item.product.id))

def delete(request, id):
    item = OrderItem.objects.get(pk=id)
    item.delete()
    return redirect('/marketplace/add_to_cart/'+str(item.product.id))
