from django.shortcuts import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Products
from api.serializers import ProductsSerializer


class ProductsListAPIView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsDetailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Products.objects.get(pk=product_id)
        except Products.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, product_id):
        instance = self.get_object(product_id)
        serializer = ProductsSerializer(instance)
        return Response(serializer.data)

    def put(self, request, product_id):
        instance = self.get_object(product_id)
        serializer = ProductsSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        instance = self.get_object(product_id)
        instance.delete()
        return Response({'deleted': True})