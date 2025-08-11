from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenBlacklistView


app_name = "blog"

router=DefaultRouter()

router.register(r"cvs",views.comentviewset,basename="cvs")
router.register(r"rocvs",views.readonlycomentviewset,basename="rocvs")
router.register(r"cs",views.comentset,basename="cs")


urlpatterns = [
   path("ms/",include(router.urls)),

   path('', views.homeview, name="homeview"),
   path('blog/<int:pk>/', views.singleblogview, name="singleblog"),
   path('blogprofile/', views.blogprofile, name="blogprofile"),
   path('createblogview/', views.createblogview, name="createblogview"),
   path('Blogsview/', views.Blogsview, name="Blogsview"),
   path('updateblogview/<int:pk>/', views.updateblogview, name="updateblogview"),
   path('apiview/', views.Apiviewset.as_view(), name="Apiview"),
   path('singleapiview/<int:pk>/', views.Singleapiviewset.as_view(), name="singleApiview"),
   path('myserializer/', views.Serializertest.as_view(), name="myserializer"),
   path('gatozlc/', views.Gatozlc.as_view(), name="gatozlc"),
   path('gatozrud/<int:pk>', views.Gatozrud.as_view(), name="gatozrud"),
   path('register/', views.registerview.as_view(), name='register'),
   path('login/',views.loginview.as_view(), name='login'),
   path("intro/",views.intro.as_view(),name="intro"),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
   path("api/changepassword/",views.password_change.as_view(),name="password_change"),
]
