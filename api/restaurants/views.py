from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Restaurants
from .serializers import RestaurantSerializer

class RestaurantList(APIView):
    def get(self, request):
        restaurants = Restaurants.objects.select_related('category', 'price_range').all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        response_code = 'success'
        http_status = status.HTTP_201_CREATED  # 생성 성공 시 201 상태 코드 사용
        messages = []
        result = None

        try:
            serializer = RestaurantSerializer(data=request.data)
            if serializer.is_valid():
                result = serializer.save()
            else:
                response_code = 'validation_failed'
                http_status = status.HTTP_400_BAD_REQUEST
                messages = serializer.errors
        except Exception as e:
            response_code = 'server_error'
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            messages = [str(e)]

        response_data = {
            'code': response_code,
            'messages': messages,
            'result': RestaurantSerializer(result).data if result else None
        }

        return Response(response_data, status=http_status)
                
class RestaurantDetail(APIView):
    def get_object(self, pk):
        try:
            return Restaurants.objects.select_related('category', 'price_range').get(pk=pk)
        except Restaurants.DoesNotExist:
            raise NotFound(detail="Restaurant not found")
            
    def get(self, request, pk):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
    def put(self, request, pk):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
