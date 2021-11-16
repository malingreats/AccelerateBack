from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from users.models import Profile

def upload_to(instance, filename):
	return filename.format(filename=filename)

class Store(models.Model):

	# SDG_One = 'SDG_One'
	# SDG_Two = 'SDG_Two'
	# SDG_Three = 'SDG_Three'
	# SDG_GOALS = [
	# 	(SDG_Two, 'SDG_Two'),
	# 	(SDG_One, 'SDG_One'),
	# 	(SDG_Three, 'SDG_Three'),
	# ]   

	vendor = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=128,blank=False)
	category = models.CharField(max_length=255, null=True, blank=True)
	desc = models.CharField(max_length=255, null=True, blank=True)
	sdg_goals = models.CharField(max_length=75,null=True, blank=True, default = 'One')
	store_logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
	rating = models.FloatField(null=True, blank=True, default=0.0)

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

	store = models.ForeignKey(Store, null=True, on_delete=models.CASCADE)
	owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, null=True, blank=True)
	desc = models.CharField(max_length=255, null=True, blank=True)
	category = models.CharField(max_length=255, null=True, blank=True)
	price  = models.FloatField(null=True, blank=True, default=0.0)
	discount = models.FloatField(null=True, blank=True, default=0.0)
	quantity = models.IntegerField(null=True, blank=True, default=0)
	tags = models.CharField(max_length=35,choices=TAGS, default = tag1, null=True, blank=True,)
	rating = models.FloatField(null=True, blank=True, default=0.0)
	date_created = models.DateTimeField(auto_now_add=True)
	is_stocked = models.BooleanField(default=True, blank=True)
	product_image = models.ImageField(upload_to=upload_to, blank=True, null=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ('-date_created',)


class Service(models.Model):

	tag1 = 'tag1'
	tag2 = 'tag2'
	tag3 = 'tag3'
	TAGS = [
		(tag2, 'tag2'),
		(tag1, 'tag1'),
		(tag3, 'tag3'),
	]    

	store = models.ForeignKey(Store, null=True, on_delete=models.CASCADE)
	owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, null=True, blank=True)
	desc = models.CharField(max_length=255, null=True, blank=True)
	category = models.CharField(max_length=255, null=True, blank=True)
	price  = models.FloatField(null=True, blank=True, default=0.0)
	discount = models.FloatField(null=True, blank=True, default=0.0)
	tags = models.CharField(max_length=35,choices=TAGS, default = tag1, null=True, blank=True,)
	rating = models.FloatField(null=True, blank=True, default=0.0)
	date_created = models.DateTimeField(auto_now_add=True)
	availability = models.BooleanField(default=True, blank=True)
	service_image = models.ImageField(upload_to=upload_to, blank=True, null=True)


	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ('-date_created',)


# class Order(models.Model):

# 	customer_name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
# 	payment_type = models.CharField(max_length=50, null=True, blank=True)
# 	quantity= models.IntegerField(null=True, blank=True, default=0)
# 	created = models.DateTimeField(auto_now_add=True)
# 	status = models.BooleanField(default=False, null=True, blank=True)
# 	products = models.TextField(null=True, blank=True)
# 	product_owner = models.CharField(max_length=255, null=True, blank=True)
# 	payer_email = models.EmailField(max_length=150, null=True, blank=True)
# 	payer_name = models.CharField(max_length=255, null=True, blank=True)
# 	payer_id  = models.CharField(max_length=255, null=True, blank=True)
# 	purchase_amount = models.FloatField(null=True, blank=True, default=0.0)
# 	shipping_address = models.TextField(null=True, blank=True,)
# 	shipping_option = models.CharField(max_length=255, null=True, blank=True)

# 	def __str__(self):
# 		return str(self.id)



class StoreOrder(models.Model):

	customer_name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	payment_type = models.CharField(max_length=50, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	total_purchase_amount = models.FloatField(null=True, blank=True, default=0.0)


	def __str__(self):
		return str(self.id)


class VendorOrder(models.Model):

	payee_name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	payment_type = models.CharField(max_length=50, null=True, blank=True)
	quantity= models.IntegerField(null=True, blank=True, default=0)
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=False, null=True, blank=True)
	products = models.TextField(null=True, blank=True)
	payer_name = models.CharField(max_length=255, null=True, blank=True)
	payer_email = models.EmailField(max_length=150, null=True, blank=True)
	payer_id  = models.CharField(max_length=255, null=True, blank=True)
	purchase_amount = models.IntegerField(null=True, blank=True, default=0.0)
	shipping_address = models.TextField(null=True, blank=True,)
	shipping_option = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.id)

	class Meta:
		ordering = ('-created',)