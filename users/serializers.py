from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer


from .models import Profile, BillingAddress

from django.core.mail import send_mail


class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'

class BillingAddressSerializer(ModelSerializer):
	class Meta:
		model = BillingAddress
		fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True)
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)
	last_name = serializers.CharField(required=True)

	class Meta:
		model = User
		fields = ('username', 'password', 'password2', 'email', 'last_name', 'first_name')

	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			last_name=validated_data['last_name'],
			first_name=validated_data['first_name']
		)

		user.set_password(validated_data['password'])
		user.save()


		# profile_user = Profile.objects.get(user = user)
		
		if validated_data['last_name'] == 'vendor':

			user.profile.is_vendor = True
			user.save()
			body = 'Hello ' + user.username + '\n \n \nWe welcome you to The Good Market \n \n' + 'To continue selling please finish setting up your Store and Personal Profile \n \n' + 'You will receive an email once your account is approved \n \n \n \n' + 'Thank You \n' + 'THE GOODMARKET TEAM \n' + ' ' + ' https://store.thegoodmarket.io'
			send_mail('Welcome', body, 'benjaminnyakambangwe@gmail.com', ['bennyakambangwe@gmail.com', user.email], fail_silently=False)
			print('Vendor', user.profile.is_vendor)
		elif validated_data['first_name'] == 'customer':
			user.profile.is_customer = True
			user.save()
			body2 = 'Hello ' + user.username + '\n \n \nWe welcome you to The Good Market \n \n' + 'To continue buying please finish setting up your Account \n \n \n' + 'Thank You \n' + 'THE GOODMARKET TEAM \n' + ' ' + ' https://store.thegoodmarket.io'
			send_mail('Welcome', body2, 'benjaminnyakambangwe@gmail.com', ['bennyakambangwe@gmail.com', user.email], fail_silently=False)
			print('Customer', user.profile.is_customer)

		return user





