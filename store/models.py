from django.db import models
from django.utils.text import slugify



class ProductModel(models.Model):
	name = models.CharField(max_length=40)
	slug = models.SlugField(blank=True)
	price = models.FloatField()
	manufacturer = models.CharField(max_length=40)
	guarantee = models.IntegerField()
	info = models.JSONField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(ProductModel, self).save(*args, **kwargs)