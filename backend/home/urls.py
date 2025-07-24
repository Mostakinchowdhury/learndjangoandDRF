from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/<int:num>/', views.about, name="about"),
    path('here/<int:num>/', views.here, name="here"),

    path("nothing/<int:num>/", views.nothing, name="nothing"),
    path("nothing/", views.nothingnot, name="nothingnot"),
    path("kichuna/", views.kichuna, name="kichuna"),
    path("test-reverse/", views.test_reverse),path("accounts/", include("django.contrib.auth.urls")),
]
