from rest_framework import generics
from rest_framework.permissions import AllowAny

from . import models
from . import serializers


class AddAuthorView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AddAuthorSerializer
    queryset = models.Author.objects.all()


class ListAuthorView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ListAuthorSerializer
    queryset = models.Author.objects.all()


class DeleteAuthorView(generics.DestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Author.objects.all()
    lookup_field = 'name'
