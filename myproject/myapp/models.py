from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    usertype = models.CharField(max_length=20,default="buyer")
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=20)
    profile = models.ImageField(default="",upload_to="pictures/")

    def __str__(self):
        return self.name
    

class Product(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    category = (
               ("Juice","Juice"),
               ("Fruits","Fruits")
               )
    
    pcategory = models.CharField(max_length=20,choices=category)
    pprice = models.PositiveIntegerField()
    pname = models.CharField(max_length=50)
    pdesc = models.TextField()
    pimage = models.ImageField(default="",upload_to="pimage/")

    def __str__(self):
        return self.pname
    


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    payment = models.BooleanField(default=False)
    cqty = models.PositiveIntegerField(default = 1)
    tprice = models.PositiveIntegerField()
    cprice = models.PositiveIntegerField()
    

    