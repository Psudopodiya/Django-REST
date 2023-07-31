from django.urls import path
from . import views

urlpatterns = [
     path('getFood/', views.getFood, name='getFood'),
    path('postFood/', views.postFood, name='postFood'),
]