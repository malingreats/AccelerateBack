from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProductSerializer
from api.models import Product


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # custom claims
        token['username'] = user.profile.full_name
        token['phone'] = user.profile.phone
        token['location'] = user.profile.location
        token['bio'] = user.profile.bio
        token['email'] = user.email
        token['is_vendor'] = user.profile.is_vendor
        token['is_customer'] = user.profile.is_customer
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
def getRoutes(request):
	routes = [
	'/api/token',
	'api/token/refresh'
	]

	return Response(routes)