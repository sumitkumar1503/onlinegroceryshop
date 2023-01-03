from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail



def home_view(request):
    mydict={
        'products':models.Product.objects.all()[:8],
        'categories':models.Category.objects.all()
    }

    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'bazaar/index.html',context=mydict)

def afterlogin_view(request):
    return redirect('admin-dashboard')


@login_required(login_url='login')

def admin_dashboard_view(request):
    mydict={
        
        'totalproduct':models.Product.objects.all().count(),
        'totalorder':models.Order.objects.all().count(),
        'totalamount':models.Order.objects.all().aggregate(Sum('price'))['price__sum'],
    }
    return render(request,'bazaar/admin_dashboard.html',context=mydict)





@login_required(login_url='login')
def delete_order_view(request,pk):
    order=models.Order.objects.get(id=pk)
    order.delete()
    return redirect('admin-order')


@login_required(login_url='login')
def admin_product_view(request):
    return render(request,'bazaar/admin_product.html')

@login_required(login_url='login')
def admin_add_category_view(request):
    form1=forms.CategoryForm()
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.CategoryForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
        else:
            print('form invalid')
        return HttpResponseRedirect('admin-view-category')
    return render(request,'bazaar/admin_add_category.html',context=mydict)

@login_required(login_url='login')
def admin_view_category_view(request):
    categories=models.Category.objects.all()
    mydict={
        'categories':categories,
    }
    return render(request,'bazaar/admin_view_category.html',context=mydict)


@login_required(login_url='login')
def delete_category_view(request,pk):
    cat=models.Category.objects.get(id=pk)
    cat.delete()
    return redirect('admin-view-category')



@login_required(login_url='login')
def update_category_view(request,pk):
    category=models.Category.objects.get(id=pk)
    form1=forms.CategoryForm(instance=category)
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.CategoryForm(request.POST,request.FILES,instance=category)
        if form1.is_valid():
            form1.save()
        else:
            print('form invalid')
        return HttpResponseRedirect('/admin-view-category')
    return render(request,'bazaar/admin_update_category.html',context=mydict)



@login_required(login_url='login')
def admin_add_product_view(request):
    form1=forms.ProductForm()
    mydict={'form1':form1,
   
    }
    if request.method=='POST':
        form1=forms.ProductForm(request.POST,request.FILES)
        if form1.is_valid():
           product= form1.save()
           product.categoryid=request.POST.get('categoryid')
           category=models.Category.objects.get(id=request.POST.get('categoryid'))
           product.categoryname=category.englishname
           product.save()
        else:
            print('form invalid')
        return HttpResponseRedirect('/admin-add-product')
    return render(request,'bazaar/admin_add_product.html',context=mydict)

@login_required(login_url='login')
def admin_view_product_view(request):
    products=models.Product.objects.all()
    mydict={
        'products':products,
    }
    return render(request,'bazaar/admin_view_product.html',context=mydict)


@login_required(login_url='login')
def delete_product_view(request,pk):
    cat=models.Product.objects.get(id=pk)
    cat.delete()
    return redirect('admin-view-product')

@login_required(login_url='login')
def update_product_view(request,pk):
    cat=models.Product.objects.get(id=pk)
    form1=forms.ProductForm(instance=cat)
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.ProductForm(request.POST,request.FILES,instance=cat)
        if form1.is_valid():
           product= form1.save()
           product.categoryid=request.POST.get('categoryid')
           category=models.Category.objects.get(id=request.POST.get('categoryid'))
           product.categoryname=category.englishname
           product.save()
        else:
            print('form invalid')
        return HttpResponseRedirect('/admin-view-product')
    return render(request,'bazaar/admin_update_product.html',context=mydict)


def customer_view_product_by_category_view(request,pk):
    category=models.Category.objects.get(id=pk)
    products=models.Product.objects.all().filter(categoryid=pk)
    mydict={
        'products':products,
        'category':category,
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'bazaar/customer_view_products_by_category.html',context=mydict)

def all_product_view(request):
    products=models.Product.objects.all()
    mydict={
        'products':products,
    }
    return render(request,'bazaar/all_product.html',context=mydict)




def order_product_view(request,pk):
    order=models.Order()
    order.product=models.Product.objects.get(id=pk)
    order.category=models.Category.objects.get(id=order.product.categoryid)
    order.price=order.product.price

    form1=forms.OrderForm()
    mydict={
        'form1':form1,
        'product':models.Product.objects.get(id=pk),
    
    }
    if request.method=='POST':
        form1=forms.OrderForm(request.POST)
        if form1.is_valid():
        
            order.mobile=request.POST.get('mobile')
            order.address=request.POST.get('address')
            order.customername=request.POST.get('customername')
            order.save()
            return render(request,'bazaar/order_placed.html',context=mydict)
    return render(request,'bazaar/place_order.html',context=mydict)




@login_required(login_url='login')
def admin_order_view(request):
    orders=models.Order.objects.all().order_by('id').reverse()
    return render(request,'bazaar/admin_order.html',{'orders':orders})


def terms_view(request):
    return render(request,'bazaar/terms.html')
def privacy_view(request):
    return render(request,'bazaar/privacy.html')
def aboutus_view(request):
    return render(request,'bazaar/aboutus.html')

