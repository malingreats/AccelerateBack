from rest_framework.serializers import ModelSerializer
from .models import Product,Service, Store, StoreOrder, VendorOrder

class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = ("id", "store", "owner", "name", "desc", "category", "price", "discount", "quantity", "tags", "rating", "date_created", "is_stocked")


class ServiceSerializer(ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'


# class OrderSerializer(ModelSerializer):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'

class StoreOrderSerializer(ModelSerializer):
	class Meta:
		model = StoreOrder
		fields = '__all__'


class VendorOrderSerializer(ModelSerializer):
	class Meta:
		model = VendorOrder
		fields = ("payee_name", "id","payment_type", "quantity", "created", "status", "products", "payer_email", "payer_name", "payer_id", "purchase_amount")


class StoreSerializer(ModelSerializer):
	class Meta:
		model = Store
		fields = '__all__'