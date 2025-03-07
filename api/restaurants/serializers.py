from rest_framework import serializers
from .models import Restaurants, Category, PriceRange

class RestaurantSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    price_range = serializers.PrimaryKeyRelatedField(queryset=PriceRange.objects.all())

    class Meta:
        model = Restaurants
        fields = [
            'idx', 
            'name', 
            'category', 
            'price_range',
            'region',
            'address', 
            'description', 
            'average_rating', 
            'number_of_ratings', 
            'phone_number',
            'opening_hours', 
            'reservation_available', 
            'updated_at', 
            'created_at'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name if instance.category else None
        representation['price_range'] = instance.price_range.label if instance.price_range else None
        return representation