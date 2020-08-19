from django.db import models
from datetime import datetime

class Admin(models.Model):
    Admin_ID = models.IntegerField(primary_key=True)
    Contact = models.IntegerField()
    Name = models.CharField(max_length=264)

    def __str__(self):
       return self.Name

class Seller(models.Model):
    Seller_ID = models.IntegerField(primary_key=True)
    Contact = models.IntegerField()
    Name = models.CharField(max_length=264)

    def __str__(self):
       return self.Name

class Buyer(models.Model):
    Buyer_ID = models.IntegerField(primary_key=True)
    Address = models.CharField(max_length=264)
    Contact = models.IntegerField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    rating = models.PositiveSmallIntegerField(default=0)
    Sex = models.CharField(max_length=6)

    def __str__(self):
       return self.first_name

class Order(models.Model):
    Order_ID = models.IntegerField(primary_key=True)
    Buyer_ID = models.ForeignKey(Buyer)
    Delivery_Date = models.DateField(auto_now=False, auto_now_add=False)
    Order_Date = models.DateField(default=False, auto_now_add=False)
    Seller_ID = models.ForeignKey(Seller)
    Total = models.DecimalField(decimal_places=2, max_digits=5)

    def __repr__(x):
       return x.Order_ID


class Product(models.Model):
    Product_ID = models.IntegerField(primary_key = True)
    Order_ID = models.ForeignKey(Order)
    Buyer_ID = models.ForeignKey(Buyer)
    Name = models.CharField(max_length=264)
    Product_Description = models.TextField()
    Reviews = models.TextField()
    Quantity = models.IntegerField(default=1)
    Total_Price = models.DecimalField(decimal_places=2, max_digits=5)
    Unit_Price = models.DecimalField(decimal_places=2, max_digits=5)
    Product_Image = models.ImageField(blank=True, null=True, upload_to="covers/%Y/%m/%D/")

    def __str__(self):
       return self.Name
