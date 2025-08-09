from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Blogs,Comment
from .forms import Blogform
from django.contrib import messages
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from .serializer import BlogSerializer,Myserializer,ComentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from rest_framework.viewsets import ModelViewSet,ViewSet,ReadOnlyModelViewSet
from rest_framework import filters
from .paginations import mypagi,myoffpagi
from django_filters.rest_framework import DjangoFilterBackend

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



# api section day 11

class Apiviewset(APIView):
   def get(self,request):
      allblogs=Blogs.objects.all().order_by("-blog_upload_time")
      serialize=BlogSerializer(allblogs,many=True)
      return Response(serialize.data,status=status.HTTP_200_OK)
   def post(self,request):
         serial=BlogSerializer(data=request.data)
         if serial.is_valid():
           serial.save()
           return Response(serial.data,status=status.HTTP_201_CREATED)
         else:
           return Response(serial.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class Singleapiviewset(APIView):
   def get(self,request,pk):
      allblogs=Blogs.objects.get(id=pk)
      serialize=BlogSerializer(allblogs)
      return Response(serialize.data,status=status.HTTP_200_OK)
   def delete(self,request,pk):
      allblogs=Blogs.objects.get(id=pk)
      serialize=BlogSerializer(allblogs)
      allblogs.delete()
      return Response(serialize.data,status=status.HTTP_200_OK)

#serializer
#



class Serializertest(APIView):
    def post(self, request):
      serialize=Myserializer(data=request.data)
      if serialize.is_valid():
          return Response(serialize.data,status=status.HTTP_201_CREATED)
      else:
        return Response(serialize.errors,status=status.HTTP_406_NOT_ACCEPTABLE)



class Gatozlc(generics.ListCreateAPIView):
  queryset=Blogs.objects.all()
  serializer_class=BlogSerializer
class Gatozrud(generics.RetrieveUpdateDestroyAPIView):
  queryset=Blogs.objects.all()
  serializer_class=BlogSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from .permission import mypermission
class comentviewset(ModelViewSet):
    queryset = Comment.objects.all()
    authentication_classes=[SessionAuthentication]
    permission_classes=[mypermission]
    serializer_class = ComentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend]
    pagination_class=mypagi
    search_fields = ['coment_text']
    ordering_fields = ['coment_date']
    ordering = ['coment_date']

from .filterset import commentFilter

class readonlycomentviewset(ReadOnlyModelViewSet):
  permission_classes=[DjangoModelPermissions,]
  queryset=Comment.objects.all()
  serializer_class=ComentSerializer
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  pagination_class=myoffpagi
  filterset_class=commentFilter
  search_fields = ['coment_text']
  ordering_fields = ['coment_date']
  ordering = ['coment_date']



class comentset(ViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

  queryset=Comment.objects.all()
  serializer_class=ComentSerializer









