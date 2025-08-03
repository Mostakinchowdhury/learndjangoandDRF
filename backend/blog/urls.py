from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
   path('', views.homeview, name="homeview"),
   path('blog/<int:pk>/', views.singleblogview, name="singleblog"),
   path('blogprofile/', views.blogprofile, name="blogprofile"),
   path('createblogview/', views.createblogview, name="createblogview"),
   path('Blogsview/', views.Blogsview, name="Blogsview"),
   path('updateblogview/<int:pk>/', views.updateblogview, name="updateblogview"),
]
