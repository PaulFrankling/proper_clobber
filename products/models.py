from django.db import models


class Category(models.Model):
    """ Product Category model """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ Returns friendly name """
        return self.friendly_name


class Product(models.Model):
    """ Product Model """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, default='', blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_clothing_sizing = models.BooleanField(
        default=False, null=True, blank=True)
    has_footwear_sizing = models.BooleanField(
        default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, default='', blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
