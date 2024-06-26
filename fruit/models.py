from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class OrderStatusTextChoices(models.TextChoices):
    ORGANIC = "Organic"
    FRESH = "Fresh"
    SALES = "Sales"
    DISCOUNT = "Discount"
    EXPIRED = "Expired"    

class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Category/")

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField() #new
    price = models.FloatField()
    rating = models.FloatField(default=4) #change
    description = models.TextField()
    weight = models.FloatField()
    country_of_origin = models.CharField(max_length=200)
    quality = models.CharField(max_length=50,choices=OrderStatusTextChoices.choices)
    checked = models.CharField(max_length=200)
    min_weight = models.FloatField()
    image = models.ImageField(upload_to="Products/")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="Products")

    def get_absolute_url(self): #new
        return reverse('detail-page', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.first_name

class Comment(models.Model):
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField()
    email = models.EmailField(max_length=100) #new
    created_date = models.DateField(auto_now=True) #new
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


# class Cart(models.Model):
#     cart_id = models.CharField(max_length=50,primary_key=True)
#     total = models.DecimalField(max_digits=9,decimal_places=2)  
#     quantity = models.IntegerField()  
#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.cart_id

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     product_quantity = models.IntegerField(default=0)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user} {self.product} {self.product_quantity}'


# --- new ---

class Cart(models.Model):
    date_added = models.DateTimeField(auto_now=True)
    session_id = models.CharField(max_length=200, default='')

   
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.product.title

    def get_total(self):
        return self.quantity * self.product.price