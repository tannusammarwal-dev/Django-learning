from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .forms import RegistrationForm
from .forms import ProductFrom
from .models import Product



# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'registration sucessfull 👍!')
            return redirect('login')

        else:
            messages.error(request,"registration failed please try again!")
            return render(request,"register.html",{'form':form})
    else:
        form =RegistrationForm() 
        return render(request,"register.html",{'form': form}) 
       

def login_view(request):
    if request.method =="POST":
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
             login(request,user)
             messages.success(request,"login successful")
             return redirect("dashboard")

        else:
             messages.error(request,"Invalid username or password")

    return render(request,"login.html")     

             


def logout_view(request):
        logout(request)
        messages.success(request,"you have been logged out")
        return redirect('login')


# @login_required(login_url ='login')
def dashboard(request):
    form = RegistrationForm()
    return render(request,"dashboard.html",{'form':form})


def dashboard(request):

    products = Product.objects.all()[:4]

    return render(request, 'dashboard.html', {
        'products': products
    }) 


def product_list(request):
        products = Product.objects.all()
        return render(request,"product_list.html",{'products':products})

def add_products(request):
    if request.method == 'POST':
        form = ProductFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductFrom()

    return render(request, 'add_products.html', {'form': form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)

    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request):
   return render(request,'cart.html')


