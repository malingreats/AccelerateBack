from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile

class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	# permission_classes = (AllowAny)
	serializer_class = RegisterSerializer


class ProfilesView(APIView):

	def get(self, request, *args, **kwargs):
		qs = Profile.objects.all()
		serializer = ProfileSerializer(qs, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ProfileSerializer(data = request.data)
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


# class VendorProfilesView(APIView):
# 	serializer_class = ProfileSerializer

# 	def get_queryset(self):
# 		queryset = Profile.objects.all()
# 		is_vendor = self.request.query_params.get('is_vendor')
# 		if is_vendor is not None:
# 			queryset = queryset.filter(is_vendor=is_vendor)
# 		return queryset
		# serializer = ProfileSerializer(queryset, many=True)
		# return Response(serializer.data)

class VendorProfilesView(generics.ListAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	filterset_fields = ('location',)

	def get(self, request, *args, **kwargs):
		qs = Profile.objects.all()
		serializer = ProfileSerializer(qs, many=True)
		return Response(serializer.data)