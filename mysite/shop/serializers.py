from rest_framework import serializers
from shop.models import User, School, Product, Category, Basket


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSer(serializers.ModelSerializer):
    category = CategorySer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SchoolSer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class BasketListSerializer(serializers.ModelSerializer):
    product = ProductSer(many=False, read_only=True)
    user = UserSer(many=False, read_only=True)

    class Meta:
        model = Basket
        fields = '__all__'
