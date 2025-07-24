from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

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
    try:
        url = reverse("auth:login")
        return HttpResponse(f"Login URL: {url}")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
