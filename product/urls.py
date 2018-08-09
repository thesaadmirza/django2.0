from django.contrib import admin
from django.urls import path
from .views import index,editProduct,deleteProduct

urlpatterns = [
    path('/',index),
    path('/editProduct/<int:id>/',editProduct,name='editProduct'),
    path('updateProduct/',editProduct,name='updateProduct'),
    path('deleteProduct/',deleteProduct,name='deleteProduct'),
]
