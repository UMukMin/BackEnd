from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurants
from .serializers import RestaurantSerializer

class RestaurantList(APIView):
    def get(self, request):
        restaurants = Restaurants.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)