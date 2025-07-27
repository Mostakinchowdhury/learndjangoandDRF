from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from django.contrib.auth import  urls
from .models  import Products_detail
from .forms import Productform
from django.contrib import messages
# from django.core import mail

def home(request):
    return HttpResponse("This is the home page")

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

