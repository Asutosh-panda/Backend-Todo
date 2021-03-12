from django.contrib import admin
from django.urls import path
from backend import views 

urlpatterns = [
    path('index',views.index,name="index"),
     path('indexpost',views.indexpost,name="indexpost"),
      path('indexput/<str:pk>',views.indexput,name="indexput"),
       path('indexdelete/<str:pk>',views.indexdelete,name="indexdelete")
]





