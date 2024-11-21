from ast import Return
from django.shortcuts import render
from .models import product_list, customer_list
from .serializers import CustomerSerailizer, ProductSerailizer
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import get_object_or_404












# Create your views here.
@api_view(['POST'])
def customerList(request):
    serializers = CustomerSerailizer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view (['GET'])
def Customer_lists(request):
    objs = customer_list.objects.all()
    serializers = CustomerSerailizer(objs, many=True)
    return Response (serializers.data)


@api_view (['GET'])
def customer(request,id):
    customer = get_object_or_404(customer_list, id=id)
    serializers = CustomerSerailizer(customer)
    return Response (serializers.data)
    

@api_view(['PUT','PATCH'])
def customer_update(request,id):
    try:
        # Fetch the existing customer instance by ID
        customer = customer_list.objects.get(id=id)
    except customer_list.DoesNotExist:
        return Response({'detail': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)
    data=request.data
    if request.method == 'PUT':
        serializers = CustomerSerailizer(customer,data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        data=request.data
        serializers=CustomerSerailizer(customer_list,data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])

def customer_delete(request,id):
    data = request.data 
    objs = customer_list.objects.get(id=id)
    objs.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

    
 
# Product-----------------------------------List
@api_view (['POST'])
def product_add(request):
    serializers= ProductSerailizer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def product_lists(request):
    objs = product_list.objects.all()
    serializers = ProductSerailizer(objs, many=True)
    return Response (serializers.data)
    
    
@api_view(['GET'])
def product(request,id):
    product = get_object_or_404(product_list, id=id)
    serializers = ProductSerailizer(product)
    return Response (serializers.data)


@api_view(['PUT','PATCH'])
def Product_update(request,id):
    try:
        product= product_list.objects.get(id=id)
        
    except product_list.DoesNotExist:
        return Response({'detail': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data=request.data 
    if request.method == 'PUT':
        serializers = ProductSerailizer(product,data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response (serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializers = ProductSerailizer(product,data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['DELETE'])
def product_delete(request,id):
    data = request.data 
    objs = product_list.objects.get(id=id)
    objs.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
