from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

def upload_to(instance, filename):
	return filename.format(filename=filename)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=200, null=True, blank=True)
	is_active = models.BooleanField(('active'), default=True)
	is_staff = models.BooleanField(('staff'), default=False)
	is_vendor = models.BooleanField(('vendor'), default=True)
	is_customer = models.BooleanField(('customer'), default=False)
	time_added = models.DateTimeField(auto_now_add=True, null=True)
	profile_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	location = models.CharField(max_length=100, null=True, blank=True)
	bio = models.TextField(null=True, blank=True)
	web_url = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True)
	orders = models.IntegerField(null=True, blank=True, default=0)

	def __str__(self):
		return str(self.full_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile = Profile.objects.create(user=instance)
		profile.save()
	else:
		instance.profile.save()

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()
