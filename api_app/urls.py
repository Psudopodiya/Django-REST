from django.urls import path
from . import views

urlpatterns = [
    path('', views.getFood),
    path('post/', views.postFood)
]