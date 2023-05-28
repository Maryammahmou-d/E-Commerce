from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .models import *
from .forms import LogInForm


def register_fun(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    data = CustomerModel(Email=email, Username=username, Password=password)
    data.save()
    return render(request, 'App1/Register.html')


def login_fun(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomerModel.objects.filter(Username=username, Password=password).first()
            if user:
                # set user session
                request.session['user_id'] = user.id
                return redirect('Home')
            else:
                # invalid login
                return render(request, 'App1/Login.html', {'form': form, 'error': 'Invalid login credentials.'})
    else:
        form = LogInForm()
        return render(request, 'App1/Login.html', {'form': form})


def logout_fun(request):
   logout(request)
   request.session.flush()
   return redirect('Login')


def home_fun(request):
   user_id = request.session['user_id']
   user = CustomerModel.objects.get(id=user_id)
   products = Product.objects.all()
   context={"products": products,
            "user": user}
   return render (request ,'App1/Home.html',context)


def payment_fun(request):
   return render (request , 'App1/Payment.html') 

def product_fun(request,id):
    products = get_object_or_404(Product,pk=id)
    context = {'name':products.name,
               'price':products.price,
               'img':products.imageURL,}
    return render(request, 'App1/Product.html', context)

# a view to add in cart
def cart_fun(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_id = request.session.get('user_id')
    if user_id:
        customer = get_object_or_404(CustomerModel, id=user_id)
        cart_item_created = CartItem.objects.get_or_create(customer=customer, product=product)
        return redirect('Cart')
    # Handle case when user_id is not found in the session
    return redirect('Login')


# a view to show cart page with items that belongs to the customer
def user_cart(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomerModel.objects.get(id=user_id)
        cart_items = CartItem.objects.filter(customer=user)
        context = {
            'user': user,
            'cart_items': cart_items
        }
        return render(request, 'App1/Cart.html', context)
