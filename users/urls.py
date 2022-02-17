from django.urls import path
from .views import PasswordTokenCheckAPI, RegisterView, ProfileView, ProfilesView, SetNewPasswordAPIView, VendorProfilesView, DeleteUserView, RetrieveUserView, BillingAddressView, ParticularProfileView, MyCustomersView, PatchProfileOrderView, AddCustomerView, PasswordTokenCheckAPI, RequestPasswordResetEmail

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('delete/<str:pk>', DeleteUserView.as_view(), name='delete'),
    path('retrieve-user/<str:pk>', RetrieveUserView.as_view(), name='retrieve-user'),
    path('address/', BillingAddressView.as_view(), name='address'),
    path('address/<str:pk>', BillingAddressView.as_view(), name='address'),
    path('profiles', ProfilesView.as_view(), name='profile'),
    path('particular-profile/', ParticularProfileView.as_view(),
         name='particular-profile'),
    path('vendor_profiles/', VendorProfilesView.as_view(), name='vendor_profile'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('my-customers/<int:pk>', MyCustomersView.as_view(), name='my-customers'),
    path('patch-profile-order/<int:pk>',
         PatchProfileOrderView.as_view(), name='patch-profile-order'),
    path('add-customer/', AddCustomerView.as_view(), name='add-customer'),

    path('request-reset-email', RequestPasswordResetEmail.as_view(),
         name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]
