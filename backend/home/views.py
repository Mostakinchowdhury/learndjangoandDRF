from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from django.contrib.auth import  urls
from .models  import Products_detail
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import customuserform
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from .middlewares import mydecorate

# from django.core import mail
User=get_user_model()

@mydecorate
def home(request):
    return render(request,"home/home.html")

def about(request, num):
    return render(request, "home/about.html", {"num": num})

def here(request, num):
    return HttpResponse(f"This is here page: {num}")

def nothing(request, num):
    return redirect("home:here", num=num)

def nothingnot(request):
    url = reverse("home:here", args=[789])
    return HttpResponse(f"you need to pass an argument: {url}")

def kichuna(request):
    myurl = reverse("home:about", args=[256])
    return redirect(myurl)

# ✅ test reverse
def test_reverse(request):
    return JsonResponse(urls,safe=False)

def products(request):
    all_products=Products_detail.objects.order_by("-last_update")
    context={"products":all_products}
    return render(request,"home/products.html",context)
def product(request,pk):
    single_products=Products_detail.objects.get(id=pk)
    context={"product":single_products}
    return render(request,"home/product.html",context)
def newproducts(request):
    if request.method == "POST":
        formdata = Productform(request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request, "✅ You successfully added a new product.")
            return redirect("home:productsucces")
        else:
            messages.error(request, "❌ Sorry, something went wrong. Failed to add product.")
            return redirect("home:productsucces")
    else:
        form = Productform()
        return render(request, "home/newproducts.html", {"form": form})

def productsucces(request):
    return render(request,"home/succes.html")
def updateform(request,pk):
    ins=Products_detail.objects.get(id=pk)
    if request.method=="POST":
        myform=Productform(data=request.POST,instance=ins)
        if myform.is_valid():
            myform.save()
            messages.success(request,"✅ Form update succesfull")
            return redirect("home:productsucces")
        else:
            messages.error(request,"❌ Sorry, something went wrong. Failed to add product.")
            return redirect("home:productsucces")
    else:
        form=Productform(instance=ins)
        return render(request,"home/productupdate.html",{"form":form})
def deleteform(request, pk):
    ins = get_object_or_404(Products_detail, id=pk)
    ins.delete()
    messages.success(request, "✅ Product Deleted Successfully.")
    return redirect('home:productsucces')

def customform(request):
    if request.method=="POST":
        myform=Myform(request.POST)
        if myform.is_valid():
            messages.success(request,"✅validated user input")
            return redirect("home:productsucces")
        else:
            return render(request,"home/customform.html",{"form":myform})
    else:
        form=Myform()
        return render(request,"home/customform.html",{"form":form})

@user_passes_test(lambda u:not u.is_authenticated,login_url="home:dashboard")
def registrationview(request):
    if request.method=="POST":
            form=customuserform(request.POST,request.FILES)
            if form.is_valid():
                user=form.save()
                login(request,user)
                return redirect("home:profile")
            else:
              return render(request,'home/customregistration.html',{"form":form})
    else:
        form=customuserform()
        return render(request,'home/customregistration.html',{"form":form})

@user_passes_test(lambda u:not u.is_authenticated,login_url="home:dashboard")
def loginview(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user != None:
           login(request,user)
           messages.success(request,"✅ success to login")
           return redirect("home:dashboard")
        else:
            messages.error(request,"🚫 sorry fail to log in information doesn't match")
    return render(request,"home/login.html")

def logoutview(request):
    logout(request)
    return redirect("home:login")
@login_required(login_url="home:login")
def dashboardview(request):
    return render(request,"home/dashboard.html")

@login_required(login_url="home:login")
def profile_view(request):
    user=request.user
    context = {
        'user': user,
    }
    return render(request,"home/profile.html",context)


