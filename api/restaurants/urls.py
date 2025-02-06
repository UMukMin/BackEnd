from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/restaurants', views.RestaurantList.as_view(), name='restaurants'),

]