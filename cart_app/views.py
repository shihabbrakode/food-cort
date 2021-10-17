from django.shortcuts import render, redirect, get_object_or_404
from cart5_app.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here

def cart_details(request, tot=0, count=0, ct_items=None):
    print('cart detailes')
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.price * i.QTY)
            count += i.QTY
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = products.objects.get(id=product_id)
    print('product id is...', product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(prodt=prod, cart=ct)
        if c_items.QTY < c_items.prodt.stock:
            c_items.QTY += 1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(prodt=prod, QTY=1, cart=ct)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id((request)))
    prod = get_object_or_404(products, id=product_id)
    print('ct is in cart list....',ct)
    c_items = items.objects.get(prodt=prod, cart=ct)
    if c_items.QTY > 1:
        c_items.QTY -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id((request)))
    prod = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')


def register(request):
    if request.method == "POST":
        user_name = request.POST['username']
        pass_word1 = request.POST['password']
        pass_word2 = request.POST['passre']
        if user_name == "":
            messages.info(request, "Sorry..! username field is empty please enter the username")
            return redirect('register')
        elif pass_word1 == "":
            messages.info(request, "Sorry..! password field is empty please enter the password")
            return redirect('register')

        elif pass_word1 == pass_word2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Sorry..! Username Already Exist Please Enter Another UserName")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=pass_word1)
                user.save()
                messages.info(request, "Successfully Registered")
                user_name = ""
                pass_word1 = ""
                pass_word2 = ""
                return redirect('register')
        else:
            messages.info(request, "Sorry..! Password does not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('Login successfully....')
            return redirect('/')
        else:
            messages.info(request, "Invalid Details")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def purchers(request):
    parcard=None
    tot=100
    parcard=items.objects.all()

    for i in parcard:
        print('loop....')
        tot += (i.prodt.price * i.QTY)
    print('total is...',tot)

    # parcard.delete()
    # print('cart list...',parcard)
    return render(request, 'purchers.html',{'cp':parcard,'tt':tot})
