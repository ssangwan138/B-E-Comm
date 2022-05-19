from pyexpat import model
from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=15)
    product_desc = models.CharField(max_length=50)
    category = models.CharField(max_length=15, default="")
    subcategory = models.CharField(max_length=15, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shopping/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=500, default="")
    email = models.CharField(max_length=40, default="")
    phoneno = models.CharField(max_length=40, default="") 
    
    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    items_json = models.CharField(max_length=5000)
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=40, default="")
    phoneno = models.CharField(max_length=40, default="") 
    zip_code = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=1000)
    timestap = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:30] + "..."

