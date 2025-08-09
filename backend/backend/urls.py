
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('',include("home.urls",namespace='home')),
    path('auth/', include('rest_framework.urls', namespace="rest_framework")),
]
