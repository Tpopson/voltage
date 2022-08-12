import requests
import json
import uuid

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View


from . forms import *
from . models import *
# from product.models import *
from userprofile.models import *
from shopcart.models import *


# Create your views here.
def index(request):
    latest = Product.objects.filter(latest=True)
    featured = Product.objects.filter(latest=True)
    slide1 = Slide.objects.get(pk=1)
    slide2 = Slide.objects.get(pk=2)
    slide3 = Slide.objects.get(pk=3)

    context = {
        'latest':latest,
        'featured':featured,
        'slide1':slide1,
        'slide2':slide2,
        'slide3':slide3,
    }
    return render(request, 'index.html', context)
    


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'index.html')


def product(request):
    product = Product.objects.all()

    return render(request, 'product.html',{'product':product})

def details(request, id):
    detail = Product.objects.get(pk=id)
    return render(request, 'details.html', {'detail':detail})


# authentication 
def signout(request):
    logout(request)
    messages.success(request, 'Signout successful!')
    return redirect('signin')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Signin successful!')
            return redirect('index')
        else:
            messages.warning(request, 'Username/Password incorrect. Kindly supply valid details')
            return redirect('signin')
    return render(request, 'signin.html')



def signup(request):
    form =  SignupForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        pix = request.POST['pix']
        form = SignupForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            newprofile = Profile(user = newuser)
            newprofile.first_name = newuser.first_name
            newprofile.last_name =  newuser.last_name
            newprofile.email = newuser.email
            newprofile.phone = phone
            newprofile.pix = pix
            newprofile.save()
            login(request, newuser)
            messages.success(request, 'Signup successful!')
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    return render(request, 'signup.html')
# authentication done


# profile 
@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username = request.user.username)
 
    context = {
        'profile':profile
    }
    return render(request, 'profile.html', context)


@login_required(login_url='signin')
def profile_update(request):
    profile = Profile.objects.get(user__username = request.user.username)
    form = ProfileUpdate(instance = request.user.profile)
    if request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successful!')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profile_update')
    context = {
        'profile':profile,
        'form':form,
    }
    return render(request, 'profileupdate.html', context)


@login_required(login_url='signin')
def password(request):
    profile = Profile.objects.get(user__username = request.user.username)
    form = PasswordForm(request.user)
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password change successful.')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('password')

    context = {
        'form':form,
        'profile':profile,
    }
    return render(request, 'profilepassword.html', context)
# profile done


@login_required(login_url='signin')
def addtocart(request):
    url = request.META.get('HTTP_REFERER')
    client_id = Profile.objects.get(user__username = request.user.username)
    cart_no = client_id.id
    if request.method == 'POST':
        chosen = request.POST.get('selectsize', None)
        quanty = int(request.POST['quantity'])
        proid = request.POST['proid']
        item = Product.objects.get(pk=proid)

        cart = ShopCart.objects.filter(user__username = request.user.username, order_placed=False)
        if cart:
            basket = ShopCart.objects.filter(product=item.id, size=chosen, user__username = request.user.username).first()
            if basket:
                basket.quantity += quanty
                basket.save()
                messages.success(request, 'Product added to basket')
            else:
                newitem = ShopCart()
                newitem.user = request.user
                newitem.product = item
                newitem.item_price = item.price
                newitem.quantity = quanty
                newitem.size = chosen
                newitem.order_code = cart_no
                newitem.order_placed = False
                newitem.save()
                messages.success(request, 'Product added to basket')
                return redirect(url)
        else:
            newcart = ShopCart()
            newcart.user = request.user
            newcart.product = item
            newcart.item_price = item.price
            newcart.quantity = quanty
            newcart.size = chosen
            newcart.order_code = cart_no
            newcart.order_placed = False
            newcart.save()
            messages.success(request, 'Product added to basket')
            return redirect(url)
    return redirect(url)


@login_required(login_url='signin')
def shopcart(request):
    profile = Profile.objects.get(user__username = request.user.username)
    shopcart = ShopCart.objects.filter(user__username = request.user.username,order_placed=False)

  
    for cart in shopcart:
        cart.amount = cart.product.price * cart.quantity
        cart.save()

    subtotal = 0
    vat = 0
    total = 0
    for cart in shopcart:
        subtotal += cart.product.price * cart.quantity
       
    vat = 0.075 * subtotal

    total = vat + subtotal

    return render(request, 'cart.html', {
        'shopcart':shopcart, 
        'profile':profile, 
        'subtotal':subtotal, 
        'vat':vat, 
        'total':total, 
        })


@login_required(login_url='signin')
def update(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        quanty = request.POST['quant']
        proid = request.POST['proid']
        newquant = ShopCart.objects.get(pk=proid)
        newquant.quantity = quanty
        newquant.save()
        messages.success(request, 'Item Quantity updated successfully!')
    return redirect(url)


@login_required(login_url='signin')
def delete_item(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        prodid = request.POST['prodid']
        item = ShopCart.objects.get(pk=prodid)
        item.delete()
        messages.success(request, 'Item successfully deleted from your order.')
    return redirect(url)



class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        cart = ShopCart.objects.filter(user__username = request.user.username, order_placed=False)

        subtotal = 0
        vat = 0
        total = 0

        for item in cart:
            subtotal += item.product.price * item.quantity
        
        vat = 0.075 * subtotal

        total = vat + subtotal

        return render(request, 'checkout.html', {
            'cart':cart,
            'total':total,
        })

# def check(request):
#     profile = Profile.objects.get(user__username = request.user.username)
#     cart = ShopCart.objects.filter(user__username = request.user.username, order_placed=False)

#     subtotal = 0
#     vat = 0
#     total = 0

#     for item in cart:
#         subtotal += item.product.price * item.quantity
       
#     vat = 0.075 * subtotal

#     total = vat + subtotal

#     return render(request, 'checkout.html', {
#         'cart':cart,
#         'profile':profile,
#         'total':total,
#     })



@login_required(login_url='signin')
def pay(request):
    if request.method == 'POST':
        api_key = 'sk_test_0c3bb25f14513ee95dcbe057e8b007f8b8480aa1'
        curl = 'https://api.paystack.co/transaction/initialize'    
        cburl = 'http://54.196.188.122/callback'       
        # cburl = 'http://localhost:8000/callback'       
        ref = str(uuid.uuid4()) 
        profile = Profile.objects.get(user__username = request.user.username)
        pay_code = profile.id  
        total = float(request.POST['total']) * 100  
        user = User.objects.get(username = request.user.username)   
        email = user.email  
        first_name = request.POST['first_name']     
        last_name = request.POST['last_name']   
        phone = request.POST['phone']   
        address = request.POST['address']
        state = request.POST['state']


        #collect data to send to paystack via call
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': ref, 'amount': int(total), 'email': email, 'callback_url': cburl, 'order_number': pay_code, 'currency': 'NGN'}

        #make a call to paystack
        try:
            r = requests.post(curl, headers=headers, json=data) #pip install requests
        except Exception:
            messages.error(request, 'Network busy, try again')
        else:
            transback = json.loads(r.text)
            rdurl = transback['data']['authorization_url']

            account = Order()
            account.user = user
            account.first_name = first_name
            account.last_name = last_name
            account.total = total/100
            account.order_placed = True
            account.phone = phone
            account.address = address
            account.state = state
            account.order_code = ref
            account.payment_code = pay_code
            account.save()
            return redirect(rdurl)
    return redirect('checkout')
    


def callback(request):
    profile = Profile.objects.get(user__username = request.user.username)
    cart = ShopCart.objects.filter(user__username = request.user.username, order_placed=False)

    for item in cart:
        item.order_placed = True
        item.save()

        product = Product.objects.get(pk=item.product.id)
        product.max -= item.quantity
        product.save()


    subtotal = 0
    vat = 0
    total = 0

    # total amount of all products if more than one item
    for item in cart:
        subtotal += item.price * item.quantity

    # vat at 7.5%
    vat = 0.075 * subtotal 

    # total amount to be charged 
    total = subtotal + vat

    context = {
        'profile':profile,
        'total':total,
    }

    return render(request, 'callback.html', context)


@login_required(login_url='signin')
def history(request):
    profile = Profile.objects.get(user__username = request.user.username)
    shopcart = ShopCart.objects.filter(user__username = request.user.username,order_placed=True)

  
    for cart in shopcart:
        cart.amount = cart.product.price * cart.quantity
        cart.save()

    subtotal = 0
    vat = 0
    total = 0
    for cart in shopcart:
        subtotal += cart.product.price * cart.quantity
       
    vat = 0.075 * subtotal

    total = vat + subtotal

    return render(request, 'history.html', {
        'shopcart':shopcart, 
        'profile':profile, 
        'subtotal':subtotal, 
        'vat':vat, 
        'total':total, 
        })