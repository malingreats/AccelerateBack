from django.contrib.auth.models import User
# from html5lib import serialize
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegisterSerializer, ProfileSerializer, BillingAddressSerializer, ResetPasswordEmailRequestSerializer
from .models import Profile, BillingAddress


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny)
    serializer_class = RegisterSerializer


class DeleteUserView(APIView):

    def delete(self, request, pk):
        qs = User.objects.get(id=pk)
        qs.delete()
        return Response('User Deleted')


class RetrieveUserView(APIView):
    def get(self, request, *args, pk):
        qs = User.objects.get(id=pk)
        serializer = RegisterSerializer(qs, many=False)
        return Response(serializer.data)


class ProfilesView(APIView):

    def get(self, request, *args, **kwargs):
        qs = Profile.objects.all().order_by(-time_added)
        serializer = ProfileSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)


class ProfileView(APIView):

    def get(self, request, pk):
        qs = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(qs, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        qs = Profile.objects.get(id=pk)
        data = request.data

        qs.full_name = data.get('full_name', qs.full_name)
        qs.phone = data.get('phone', qs.phone)
        qs.location = data.get('location', qs.location)
        qs.bio = data.get('bio', qs.bio)
        qs.web_url = data.get('web_url', qs.web_url)
        qs.address = data.get('address', qs.address)
        qs.email = data.get('email', qs.email)
        qs.profile_image = data.get('profile_image', qs.profile_image)

        qs.save()
        serializer = ProfileSerializer(qs)

        return Response(serializer.data)


class PatchProfileOrderView(APIView):
    def patch(self, request, pk):
        qs = Profile.objects.get(id=pk)

        qs.orders += 1
        qs.save()
        serializer = ProfileSerializer(qs)

        return Response(serializer.data)


class ParticularProfileView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        # print(user)
        return Profile.objects.filter(user=user)


class VendorProfilesView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        is_vendor = self.request.query_params.get('is_vendor', None)
        # print(is_vendor)
        return Profile.objects.filter(is_vendor=is_vendor)

# 	def get_queryset(self):
# 		queryset = Profile.objects.all()
# 		is_vendor = self.request.query_params.get('is_vendor')
# 		if is_vendor is not None:
# 			queryset = queryset.filter(is_vendor=is_vendor)
# 		return queryset
# 		serializer = ProfileSerializer(queryset, many=True)
# 		return Response(serializer.data)

# class VendorProfilesView(generics.ListAPIView):
# 	queryset = Profile.objects.all()
# 	serializer_class = ProfileSerializer
# 	filterset_fields = ('location',)

# 	def get(self, request, *args, **kwargs):
# 		qs = Profile.objects.all()
# 		serializer = ProfileSerializer(qs, many=True)
# 		return Response(serializer.data)


class MyCustomersView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        qs = profile.customers.all()

        customer = []
        for q in qs:
            cus = Profile.objects.filter(user=q)
            for cu in cus:
                cu.time_added = cu.time_added.strftime("%m/%d%Y")
                # print(cu.time_added)
            # print(cus[0])
            customer.append(cus[0])
        serializer = ProfileSerializer(customer, many=True)
        return Response(serializer.data)


class AddCustomerView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def post(self, request):
        order = request.data

        payee_name = order.get('payee_name')
        payer_name = order.get('payer_name')
        customer = order.get('customer')

        profile = Profile.objects.get(id=payee_name)
        qs = profile.customers.all()

        for q in qs:
            if str(q) == str(payer_name):
                # print("Already a Customer")
                return 1

        profile.customers.add(customer)
        # print("Customer Added")
        return Response(order)


class BillingAddressView(generics.ListAPIView):
    serializer_class = BillingAddressSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        return BillingAddress.objects.filter(name=name)

    def post(self, request, format=None):
        serializer = BillingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

    def patch(self, request, pk):
        qs = BillingAddress.objects.get(address_id=pk)
        data = request.data

        qs.destination = data.get('destination', qs.destination)
        qs.building = data.get('building', qs.building)
        qs.street = data.get('street', qs.street)
        qs.country = data.get('country', qs.country)
        qs.post = data.get('post', qs.post)
        qs.city = data.get('city', qs.city)
        qs.state = data.get('state', qs.state)
        qs.phone = data.get('phone', qs.phone)
        qs.isDefault = data.get('isDefault', qs.isDefault)

        qs.save()
        serializer = BillingAddressSerializer(qs)

        return Response(serializer.data)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        data = {'request': request, 'data': request.data}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uid64, token):
        pass
