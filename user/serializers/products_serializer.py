from rest_framework import serializers
from ..models import  *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = serializers.ALL_FIELDS

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = serializers.ALL_FIELDS


class ProductLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLocation
        fields = serializers.ALL_FIELDS
