from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurants
from .serializers import RestaurantSerializer
from django.db import transaction  

class RestaurantList(APIView):
    def get(self, request):
        restaurants = Restaurants.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
def post(self, request):
        # 요청 데이터(request.data)를 출력합니다. 주로 디버깅 용도로 사용됩니다.
        print(request.data)

        # 데이터베이스 트랜잭션 시작. atomic 블록 내의 모든 데이터베이스 작업이
        # 하나의 트랜잭션으로 처리됩니다.  중간에 오류가 발생하면 모든 변경 사항이 롤백됩니다.
        with transaction.atomic():
            # 요청 데이터에 'field' 키가 있는지 확인합니다.
            if 'field' in request.data:
                # 'field' 키가 있다면 Restaurants 모델에 새로운 레코드를 생성합니다.
                # request.data['field'] 값을 Restaurants 모델의 field 필드에 저장합니다.
                Restaurants.objects.create(field=request.data['field'])
            else:
                # 'field' 키가 없다면 400 (Bad Request) 응답을 반환합니다.
                # {"error": "Field is required"} 는 JSON 형식의 오류 메시지입니다.
                return Response({"error": "Field is required"}, status=400)

        # 요청 데이터를 RestaurantSerializer를 사용하여 직렬화합니다.
        # 직렬화는 Python 객체를 JSON과 같은 형식으로 변환하는 과정입니다.
        serializer = RestaurantSerializer(data=request.data)

        # 직렬화된 데이터가 유효한지 확인합니다.
        if serializer.is_valid():
            # 데이터가 유효하다면 직렬화된 데이터를 데이터베이스에 저장합니다.
            serializer.save()
            # 201 (Created) 응답을 반환하고, 직렬화된 데이터를 함께 반환합니다.
            return Response(serializer.data, status=201)

        # 데이터가 유효하지 않다면 400 (Bad Request) 응답을 반환하고,
        # serializer.errors (에러 메시지)를 함께 반환합니다.
        return Response(serializer.errors, status=400)