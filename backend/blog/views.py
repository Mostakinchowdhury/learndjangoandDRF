from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Blogs
from .forms import Blogform
from django.contrib import messages
from django.http import HttpResponseForbidden

User=get_user_model()

# Create your views here.

@login_required(login_url="home:login")
def homeview(request):
  myblogs=Blogs.objects.all().order_by("-blog_upload_time")
  contex={"blogs":myblogs,"user":request.user}
  return render(request,"blog/home.html",context=contex)
@login_required(login_url="home:login")
def Blogsview(request):
  myblogs=Blogs.objects.filter(blog_owner=request.user).order_by("-blog_upload_time")
  contex={"blogs":myblogs,"user":request.user}
  return render(request,"blog/blogs.html",context=contex)

@login_required(login_url="home:login")
def createblogview(request):
  if request.method=="POST":
     form = Blogform(request.POST, request.FILES, user=request.user)
     if form.is_valid():
       form.save()
       messages.success(request, "✅ blogs create succesfull")
       return redirect("home:blog:Blogsview")
     else:
       messages.error(request, "🚫 sorry to create blogs")
       return render(request, "blog/createblogs.html", {"form": form})
  else:
    myform = Blogform(user=request.user)
    return render(request, "blog/createblogs.html", {"form": myform})
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

@login_required(login_url="home:login")
def updateblogview(request, pk):
    myinstance = get_object_or_404(Blogs, id=pk)

    if myinstance.blog_owner != request.user:
        return HttpResponseForbidden("⛔ আপনি এই ব্লগটি আপডেট করার অনুমতি পাননি!")

    if request.method == "POST":
        form = Blogform(request.POST, request.FILES, user=request.user, instance=myinstance)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ ব্লগ সফলভাবে আপডেট হয়েছে")
            return redirect("home:blog:updateblogview",pk)
        else:
            messages.error(request, "🚫 ব্লগ আপডেট করা যায়নি")
            return render(request, "blog/updateblogs.html", {"form": form})
    else:
        myform = Blogform(user=request.user, instance=myinstance)
        return render(request, "blog/updateblogs.html", {"form": myform})


from django.shortcuts import get_object_or_404

@login_required(login_url="home:login")
def singleblogview(request, pk):
  myblog = get_object_or_404(Blogs, id=pk)
  return render(request, "blog/singleblog.html", {"blog": myblog})


@login_required(login_url="home:login")
def blogprofile(request):
  user = request.user
  totalpost=Blogs.objects.filter(blog_owner=user).count()
  recentpost = Blogs.objects.filter(blog_owner=user).order_by("-blog_upload_time")[0:2]
  return render(request, "blog/profile.html", {"recentpost": recentpost, "user": user,"totalpost":totalpost})


