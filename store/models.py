from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=200 , blank=True , null=True)
    slug = models.SlugField(max_length=200)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="Products", on_delete=models.CASCADE)
    title = models.CharField(max_length=200 , blank=True , null=True)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField(max_length=200 , blank=True , null=True)
    address = models.CharField(max_length=200 , blank=True , null=True)
    credit_card = models.CharField(max_length=200 , blank=True , null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
