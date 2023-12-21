from rest_framework import generics
from rest_framework.permissions import AllowAny

from . import models
from . import serializers


class AddCategoryView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AddCategorySerializer
    queryset = models.Category.objects.all()


class ListCategorView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ListCategorySerializer
    queryset = models.Category.objects.all()


class DeleteCategoryView(generics.DestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Category.objects.all()
    lookup_field = 'title'
