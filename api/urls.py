from django.urls import path
from . import views
from .views import MyTokenObtainPairView, ParticularProductsView, ParticularServicesView, PatchStoreView, SearchStoreView, SearchSDGStoreView, ParticularOrdersView, DashboardOrderView, CustomerOrderView, ChartBarDataView, PatchProductQuantityView


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
	path('patch-product-quantity/<str:pk>', PatchProductQuantityView.as_view(), name='patch-product-quantity'),


	path('services', views.getServices, name='services'),
	path('part-services/', ParticularServicesView.as_view(), name='part-services'),
	path('all-services', views.getAllServices, name='all-services'),
	path('delete-service/<str:pk>/', views.deleteService, name='delete-service'),
	path('add-service/', views.addService, name='add-service'),


	# path('order/<str:pk>', views.getOrder, name='order'),
	# path('orders/', views.getOrders, name='orders'),
	path('add-order/', views.addOrder, name='add-order'),
	# path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),
	path('all-vendor-orders/', views.getVendorOrders, name='all-vendor-orders'),
	path('vendor-order/', ParticularOrdersView.as_view(), name='vendor-order'),
	path('dash-vendor-order/', DashboardOrderView.as_view(), name='dash-vendor-order'),
	path('customer-vendor-order/', CustomerOrderView.as_view(), name='customer-vendor-order'),

	path('chartbar-data/<str:payee_name>', ChartBarDataView.as_view(), name='chartbar-data'),



	path('stores/', views.getStores, name='stores'),
	path('real-stores', views.getRealStores, name='real-stores'),
	path('single-store/<str:pk>', views.getSingleStore, name='single-store'),
	path('search-store/', SearchStoreView.as_view(), name='search-store'),
	path('search-sdg-store/', SearchSDGStoreView.as_view(), name='search-sdg-store'),
	path('patch-store/<str:pk>/', PatchStoreView.as_view(), name='patch-store'),

	

	# path('paynow/', PayNowView.as_view(), name='paynow'),


	path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]