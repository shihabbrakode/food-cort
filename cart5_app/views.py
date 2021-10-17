from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator ,EmptyPage,InvalidPage


# Create your views here.
# def test(request):
#     return render(request,'register.html')


def proDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
        print('cart datailes..def...')
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})

def test(request):
    dis=products.objects.all()
    return render(request,'cart.html',{'dis':dis})

def home(request,c_slug=None):
    print('hoame .. def')
    print('csluge is..',c_slug)
    c_page=None
    prodt=None
    pri=120
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        print("c_sluge is..",c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:
        prodt=products.objects.all().filter(available=True)
        print("prodt is.....",prodt)
        print('price is ...',pri)
    cat=categ.objects.all()
    print('categ is...',cat)

    paginator=Paginator(prodt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
        print("pro..is........",pro)

    except(EmptyPage,InvalidPage):
        pro=paginator.page((paginator.num_pages))
    return render(request,'home.html',{'pr':prodt,'ct':cat,'pg':pro})

def serching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'serch.html',{'qr':query,'pr':prod})