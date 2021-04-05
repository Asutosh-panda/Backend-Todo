from django.contrib import admin
from django.urls import path,include
from backend import views 
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from .views import current_user, UserList
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('index',views.index,name="index"),
     path('indexpost',views.indexpost,name="indexpost"),
      path('indexput/<str:pk>',views.indexput,name="indexput"),
       path('indexdelete/<str:pk>',views.indexdelete,name="indexdelete"),
       path('rest-auth/',include('rest_auth.urls')),
       path('getuser',views.getuser,name="getuser"),
       path('registerpage',views.registerpage,name="registerpage"),
        path('token-auth/', obtain_jwt_token),
              path('current_user/', current_user),
    path('users/', UserList.as_view()),
      path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]








