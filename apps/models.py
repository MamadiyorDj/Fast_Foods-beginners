from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, blank=True)
    password = models.CharField(max_length=100, blank=True)
    phone_number = PhoneNumberField(blank=True)
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    birth_date = models.DateTimeField(auto_now_add=True)
    Users_role = {
        "S": "Super admin",
        "O": "Ofitsiant",
        "U": "User",
    }
    user_role = models.CharField(max_length=1, choices=Users_role, default="U")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to ='uploads')
    price = models.IntegerField(default=0)
    description = models.TextField()
    active =  models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Fastfoods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=13)
    longitude = models.DecimalField(max_digits=17, decimal_places=13)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    fastfood_id = models.ForeignKey(Fastfoods, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    delivery_address = models.CharField(max_length=150, blank=True)
    delivery_phone = PhoneNumberField(blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=13)
    longitude = models.DecimalField(max_digits=17, decimal_places=13)

    def __str__(self):
        return self.user_id.username

    class Meta:
        ordering = ['-id']



class Order_items(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.RESTRICT, blank=True)
    product_id = models.ForeignKey(Products, on_delete=models.RESTRICT, blank=True)
    quantity = models.IntegerField(default=0, blank=True)
    # total = models.IntegerField(default=0, blank=True)
    # delivery_time = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.order_id.user_id.username


    class Meta:
        ordering = ['-id']

