from dataclasses import fields
from rest_framework import serializers
from .models import product_list, customer_list


class CustomerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = customer_list
        fields = '__all__'
        

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = product_list
        fields = '__all__'