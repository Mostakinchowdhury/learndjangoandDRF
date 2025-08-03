from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "home"

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/',include("blog.urls",namespace='blog')),
    path('about/<int:num>/', views.about, name="about"),
    path('here/<int:num>/', views.here, name="here"),
    path('customform/', views.customform, name="customform"),
    path('product/<int:pk>/', views.product, name="product"),
    path('updateform/<int:pk>/', views.updateform, name="updateform"),
    path('deleteform/<int:pk>/', views.deleteform, name="deleteform"),
    path('productsucces/', views.productsucces, name="productsucces"),
    path('products', views.products, name="products"),
    path('newproducts', views.newproducts, name="newproducts"),
    path("nothing/<int:num>/", views.nothing, name="nothing"),
    path("nothing/", views.nothingnot, name="nothingnot"),
    path("kichuna/", views.kichuna, name="kichuna"),
    path("test-reverse/", views.test_reverse),
    path("registrationview/", views.registrationview,name="registration"),
    path("loginview/", views.loginview,name="login"),
    path("logoutview/", views.logoutview,name="logout"),
    path("dashboard/", views.dashboardview,name="dashboard"),
     path('profile/', views.profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
