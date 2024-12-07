from rest_framework import serializers

from .models import Product, User


class ProductSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=200)
    quantity = serializers.FloatField(default=0)
    price = serializers.FloatField(default=0)
    category = serializers.CharField()
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category', 'user_id']

    def create(self, validated_data):
        # Define how a new `Product` object should be created
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update instance with validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
