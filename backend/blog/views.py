from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Blogs,Comment
from .forms import Blogform
from django.contrib import messages
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from .serializer import BlogSerializer,Myserializer,ComentSerializer,registerserializer,loginserializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from rest_framework.viewsets import ModelViewSet,ViewSet,ReadOnlyModelViewSet
from rest_framework import filters
from .paginations import mypagi,myoffpagi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny,IsAuthenticated

User=get_user_model()

# Create your views here.

class registerview(APIView):
  permission_classes=[AllowAny,]
  def post(self,request):
    serialize=registerserializer(data=request.data)
    if serialize.is_valid():
      mydata=serialize.save()
      return Response({"message":"user created succesfully",**mydata},status=status.HTTP_201_CREATED)
    else:
      return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
  def get(self,request):
    if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    serialize=registerserializer(request.user)
    return Response(serialize.data,status=status.HTTP_200_OK)

class loginview(APIView):
  permission_classes=[AllowAny,]
  def post(self,request):
    serialize=loginserializer(data=request.data)
    if serialize.is_valid(raise_exception=True):
      token=serialize.validated_data.get("token")
      return Response({"token":token,"message":"success to log in"},status=status.HTTP_200_OK)
    else:
      return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
from .serializer import ChangePasswordSerializer
class password_change(APIView):
  permission_classes=[IsAuthenticated,]
  def post(self,request):
    serialize=ChangePasswordSerializer(data=request.data, context={'user': request.user})
    if serialize.is_valid(raise_exception=True):
      serialize.save()
      return Response({'message':"your password changed succesfull"},status=status.HTTP_205_RESET_CONTENT)
    else:
      return Response(serialize.errors,status=status.HTTP_304_NOT_MODIFIED)
from rest_framework_simplejwt.tokens import RefreshToken
class logout(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request):
     try:
       refresh=RefreshToken(request.data["refresh"])
       refresh.blacklist()
       return Response({'message':"token add to blacklish and you are succesfully logout"},status=status.HTTP_205_RESET_CONTENT)
     except Exception as e:
       return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


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
from rest_framework.permissions import IsAuthenticated
class comentviewset(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class = ComentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend]
    pagination_class=mypagi
    search_fields = ['coment_text']
    ordering_fields = ['coment_date']
    ordering = ['coment_date']


class intro(APIView):
  permission_classes=[IsAuthenticated]
  def get(self,request):
    serialize=registerserializer(request.user)
    return Response(serialize.data)

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

from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from .serializer import blogapi
from django.core.mail import send_mail
import random
import string

def genaretrandom(length=6):
  # capital=random.choices(string.ascii_uppercase,k=2)
  # lower=random.choices(string.ascii_lowercase,k=2)
  # punc=random.choices(string.punctuation,k=1)
  num=random.choices(string.digits,k=length)
  # ramin=length-6
  # remain_latter=random.choices(string.ascii_letters+string.digits+string.punctuation,k=ramin)
  # password_listed=[*capital,*lower,*punc,*remain_latter,*num]
  random.shuffle(num)
  return "".join(num)

class apiblogsview(ModelViewSet):
  queryset=Blogs.objects.all()
  parser_classes=[MultiPartParser,FormParser]
  renderer_classes=[JSONRenderer]
  permission_classes=[IsAuthenticated]
  serializer_class=blogapi

# only get user blog's
  @action(detail=True,url_path="change_text",url_name="change_text")
  def myblog(self,request,pk):
    myblgo=self.get_object()
    if myblgo.blog_owner != request.user:
      return Response({"message":"Bokachoda mainser post edit korar ato sokh tor kene re haa?"},status=status.HTTP_403_FORBIDDEN)
    serialize=self.get_serializer(myblgo)
    myblgo.blog_text="we send a mail to your email chowdhurymostakin02@gmail.com"
    otp=genaretrandom(length=6)
    send_mail(
            subject="Your OTP Code",
            message=f"Your OTP is {otp}",
            from_email="chowdhurymostakin02@gmail.com",  # settings.py এর EMAIL_HOST_USER
            recipient_list=["chowdhurymn8@gmail.com","monirachowdhury990@gmail.com"],
            fail_silently=False,
        )
    myblgo.save()
    return Response(serialize.data,status=status.HTTP_200_OK)












