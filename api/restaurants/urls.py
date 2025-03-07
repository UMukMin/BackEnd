from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/restaurants', views.RestaurantList.as_view(), name='restaurants'),
    path('api/v1/restaurants/<int:pk>', views.RestaurantDetail.as_view(), name='restaurant_detail'),

]