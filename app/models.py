from ast import mod
from django.db import models

# Create your models here.
class product_list(models.Model):
    product_name= models.CharField(max_length=50)
    product_number= models.IntegerField( unique=True)
    product_price= models.DecimalField(max_digits=10, decimal_places=2)
    availability= models.BooleanField(default=True)
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name



class customer_list(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_number = models.IntegerField( unique=True)
    customer_ph_number = models.IntegerField(unique=True)
    purchased_date = models.DateField()
    total_spend = models.DecimalField(decimal_places=2, max_digits=10)
    
    
def __str__(self):
    return self.customer_name
    