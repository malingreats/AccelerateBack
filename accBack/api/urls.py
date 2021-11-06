from django.urls import path
from . import views
from .views import MyTokenObtainPairView, ParticularProductsView, PatchStoreView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
	path('', views.getRoutes),

	path('products', views.getProducts, name='products'),
	path('all-products', views.getAllProducts, name='all-products'),
	path('delete-product/<str:pk>/', views.deleteProduct, name='delete-product'),
	path('add-products/', views.addProducts, name='add-products'),
	path('get-products/', ParticularProductsView.as_view(), name='get-producs'),

	path('services', views.getServices, name='services'),
	path('all-services', views.getAllServices, name='all-services'),
	path('delete-service/<str:pk>/', views.deleteService, name='delete-service'),
	path('add-service/', views.addService, name='add-service'),


	path('order/<str:pk>', views.getOrder, name='order'),
	path('orders/', views.getOrders, name='orders'),
	path('add-order/', views.addOrder, name='add-order'),
	path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),


	path('stores/', views.getStores, name='stores'),
	path('patch-store/', PatchStoreView.as_view(), name='patch-store'),
	# path('patch-store/<str:pk>/', views.patchStore, name='patch-store'),


	path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]