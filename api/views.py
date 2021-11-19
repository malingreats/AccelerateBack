from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from paynow import Paynow
from datetime import datetime


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProductSerializer, ServiceSerializer, StoreSerializer, VendorOrderSerializer
from api.models import Product, Service, Store, VendorOrder


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


class ParticularServicesView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        store = self.request.query_params.get('store', None)
        print(store)
        return Service.objects.filter(store=store)






# @api_view(['GET'])
# def getOrders(request):
#     qs = Order.objects.all()
#     serializer = OrderSerializer(qs, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getOrder(request, pk):
#     qs = Order.objects.get(id=pk)
#     serializer = OrderSerializer(qs, many=False)
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteOrder(request, pk):
#     order = Order.objects.get(id=pk)
#     order.delete()
#     return Response('Order Deleted')




@api_view(['POST'])
def addOrder(request):
    serializer = VendorOrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)

@api_view(['GET'])
def getVendorOrders(request):
    qs = VendorOrder.objects.all()
    for q in qs :
        q.created = q.created.strftime('%B')
    serializer = VendorOrderSerializer(qs, many=True)
    return Response(serializer.data)


class DashboardOrderView(generics.ListAPIView):
    serializer_class = VendorOrderSerializer

    def get_queryset(self):
        payee_name = self.request.query_params.get('payee_name', None)
        print(payee_name)
        return VendorOrder.objects.filter(payee_name=payee_name)


class CustomerOrderView(generics.ListAPIView):
    queryset = VendorOrder.objects.all()
    serializer_class = VendorOrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^payer_name']


class ParticularOrdersView(generics.ListAPIView):
    serializer_class = VendorOrderSerializer

    def get_queryset(self):
        payee_name = self.request.query_params.get('payee_name', None)
        print(payee_name)
        results = VendorOrder.objects.filter(payee_name=payee_name)

        total = 0.0
        print(results)
        for result in results:
            # print(result.purchase_amount)
            total = 0.0
            total += result.purchase_amount
        total = str(total)
        print('total')
        print(total)
        # return total
        serializer = total
        return total








@api_view(['GET'])
def getStores(request):
    qs = Store.objects.all()
    serializer = StoreSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRealStores(request):
    qs = Store.objects.all()
    qs = Store.objects.filter(vendor__is_vendor=True)
    serializer = StoreSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleStore(request, pk):
    qs = Store.objects.get(id=pk)
    serializer = StoreSerializer(qs, many=False) 
    return Response(serializer.data)


class SearchStoreView(generics.ListAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']

class SearchSDGStoreView(generics.ListAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^sdg_goals']


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




# class PayNowView(APIView):
#     paynow = Paynow(
#     '12884', 
#     '3fba233a-b62e-429a-a9ea-611ad6273e9a',
#     'http://localhost:3000/', 
#     'http://localhost:3000/'
#     )

#     payment = paynow.create_payment('Order #123', 'joshua@example.com')
#     payment.add('Bananas', 2.50)

#     response = paynow.send_mobile(payment, '0771111111', 'ecocash')

#     if(response.success):
#         poll_url = response.poll_url

#         print("Poll Url: ", poll_url)

#         status = paynow.check_transaction_status(poll_url)

#         time.sleep(30)

#         print("Payment Status: ", status.status)



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






@api_view(['GET'])
def getRoutes(request):
	routes = [
	'/api/token',
	'api/token/refresh'
	]

	return Response(routes)