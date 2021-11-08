from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from paynow import Paynow


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProductSerializer, OrderSerializer, ServiceSerializer, StoreSerializer
from api.models import Product, Order, Service, Store


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # custom claims
        token['username'] = user.username
        token['phone'] = user.profile.phone
        token['location'] = user.profile.location
        token['bio'] = user.profile.bio
        token['email'] = user.email
        token['web_url'] = user.profile.web_url
        token['address'] = user.profile.address
        token['is_vendor'] = user.profile.is_vendor
        token['is_customer'] = user.profile.is_customer
        token['is_staff'] = user.profile.is_staff
        token['store_id'] = user.profile.id
        token['id'] = user.id

        # token['profile_image'] = user.profile.profile_image
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):
    user = request.user
    products = user.profile.product_set.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllProducts(request):
    qs = Product.objects.all()
    serializer = ProductSerializer(qs, many=True)
    return Response(serializer.data)

class ParticularProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        store = self.request.query_params.get('store', None)
        print(store)
        return Product.objects.filter(store=store)


@api_view(['DELETE'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product Deleted')


@api_view(['POST'])
def addProducts(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)








@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getServices(request):
    user = request.user
    service = user.profile.service_set.all()
    serializer = ServiceSerializer(service, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllServices(request):
    qs = Service.objects.all()
    serializer = ServiceSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteService(request, pk):
    service = Service.objects.get(id=pk)
    service.delete()
    return Response('Service Deleted')

@api_view(['POST'])
def addService(request):
    serializer = ServiceSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)








@api_view(['GET'])
def getOrders(request):
    qs = Order.objects.all()
    serializer = OrderSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOrder(request, pk):
    qs = Order.objects.get(id=pk)
    serializer = OrderSerializer(qs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addOrder(request):
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response('Order Deleted')






@api_view(['GET'])
def getStores(request):
    qs = Store.objects.all()
    serializer = StoreSerializer(qs, many=True)
    return Response(serializer.data)


class SearchStoreView(generics.ListAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']


class PatchStoreView(generics.ListAPIView):


    def patch(self, request, pk):
        qs = Store.objects.get(id=pk)
        data = request.data

        qs.name = data.get('name', qs.name)
        qs.sdg_goals = data.get('sdg_goals', qs.sdg_goals)
        qs.store_logo = data.get('store_logo', qs.store_logo)
        qs.desc = data.get('desc', qs.desc)
        qs.category = data.get('category', qs.category)

        qs.save()
        serializer = StoreSerializer(qs)

        return Response(serializer.data)







# class ProductAddView(APIView):

#     def post(self, request ):
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# class ProductDeleteView(APIView):

#     def delete(self, request, pk, format=None):
#         qs = Product.objects.get(pk)
#         qs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




paynow = Paynow(
    '12884', 
    '3fba233a-b62e-429a-a9ea-611ad6273e9a',
    'http://google.com', 
    'http://google.com'
    )

payment = paynow.create_payment('Order #100', 'test@example.com')

payment.add('Bananas', 2.50)
payment.add('Apples', 3.40)

response = paynow.send(payment)




@api_view(['GET'])
def getRoutes(request):
	routes = [
	'/api/token',
	'api/token/refresh'
	]

	return Response(routes)