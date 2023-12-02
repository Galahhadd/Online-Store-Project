from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model



class ProductModel(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, blank=True, max_length=255)
	price = models.FloatField()
	manufacturer = models.CharField(max_length=255)
	guarantee = models.IntegerField()
	info = models.JSONField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(ProductModel, self).save(*args, **kwargs)


class Customer(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	address = models.ForeignKey('ShippingAdressModel', on_delete=models.CASCADE, blank=True,null=True)
	

	def __str__(self):
		return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class CartItemModel(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
	product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, blank=True,null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name

class CartModel(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
	products = models.ManyToManyField(CartItemModel, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, blank=False, null=True)
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.id)


class ShippingAdressModel(models.Model):
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	zipcode = models.CharField(max_length=200, null=True)
	date_added= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address