from rest_framework.serializers import ModelSerializer
from .models import Product, Order, Service, Store

class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ("id", "store", "owner", "name", "desc", "category", "price", "discount", "quantity", "tags", "rating", "date_created", "is_stocked")


class ServiceSerializer(ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'


class OrderSerializer(ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'


class StoreSerializer(ModelSerializer):
	class Meta:
		model = Store
		fields = '__all__'