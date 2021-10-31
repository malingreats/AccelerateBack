from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from users.models import Profile

class Store(models.Model):

	SDG_One = 'SDG_One'
	SDG_Two = 'SDG_Two'
	SDG_Three = 'SDG_Three'
	SDG_GOALS = [
		(SDG_Two, 'SDG_Two'),
		(SDG_One, 'SDG_One'),
		(SDG_Three, 'SDG_Three'),
	]   

	vendor = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=128,blank=False)
	category = models.CharField(max_length=255, null=True, blank=True)
	sdg_goals = models.CharField(max_length=35,choices=SDG_GOALS, default = SDG_One)

	def __str__(self):
		return str(self.name)

@receiver(post_save, sender=Profile)
def create_store(sender, instance, created, **kwargs):
	if created:
		store = Store.objects.create(vendor=instance)
		store.save()
	# else:
	# 	instance.store.save()		

# @receiver(post_save, sender=Profile)
# def save_store(sender, instance, **kwargs):
# 	instance.store.save()


class Product(models.Model):

	tag1 = 'tag1'
	tag2 = 'tag2'
	tag3 = 'tag3'
	TAGS = [
		(tag2, 'tag2'),
		(tag1, 'tag1'),
		(tag3, 'tag3'),
	]    

	store = models.ForeignKey(Store,null=True, on_delete=models.CASCADE)
	owner = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, null=True, blank=True)
	desc = models.CharField(max_length=255, null=True, blank=True)
	category = models.CharField(max_length=255, null=True, blank=True)
	price  = models.FloatField(null=True, blank=True, default=0.0)
	discount = models.FloatField(null=True, blank=True, default=0.0)
	quantity = models.IntegerField(null=True, blank=True, default=0)
	tags = models.CharField(max_length=35,choices=TAGS, default = tag1)
	rating = models.FloatField(null=True, blank=True, default=0.0)
	date_created = models.DateTimeField(auto_now_add=True)
	is_stocked = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name)