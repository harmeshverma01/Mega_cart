from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product


# Create your views here.


class ProductView(APIView):
    serializer_class = ProductSerializer
    
    def get(self, request, id=None):
        product = Product.objects.all()
        serializer = self.serializer_class(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def patch(self, request, id=None):
        try:
            product = Product.objects.get(id=id)
            serializer = self.serializer_class(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors)
        except:
            return Response(({'details' : 'product does not Found'}), status=status.HTTP_404_NOT_FOUND)
        
        
class ProductDetails(APIView):
    serializer_class = ProductSerializer()
    
    
    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = self.serializer_class(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
                