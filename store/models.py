from django.db import models
from django.utils.text import slugify



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