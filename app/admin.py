from django.contrib import admin
from .models import product_list, customer_list

# Basic registration of the models
admin.site.register(customer_list)
admin.site.register(product_list)