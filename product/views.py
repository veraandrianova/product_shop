from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer
from .exceptions import CustomException


class ProductView(APIView):
    """Вывод списка продуктов"""
    serializer_class = ProductSerializer

    def get(self, request):
        if self.request.user.is_authenticated:
            queriset = Product.objects.all()
            serializer = ProductSerializer(queriset, many=True)
            return Response(serializer.data)
        raise CustomException
