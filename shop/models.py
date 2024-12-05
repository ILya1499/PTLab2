from django.db import models

# Create your models here.
class Promocode(models.Model):
    number = models.CharField(max_length=200)
    date_end = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    promid = models.ForeignKey(Promocode, on_delete=models.CASCADE,blank=True,null=True)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

