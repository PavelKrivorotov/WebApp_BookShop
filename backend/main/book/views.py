from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers
from . import filters


class AddBookView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AddBookSerializer
    queryset = models.Book.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializers.ListBookSerializer(instance).data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    
    def perform_create(self, serializer):
        return serializer.save()


class SetBookView(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SetBookSerializer
    queryset = models.Book.objects.all()
    lookup_field = 'isbn'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(
            serializers.ListBookSerializer(instance).data
        )


# New!
class GetBookView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ListBookSerializer
    queryset = models.Book.objects.all()
    lookup_field = 'isbn'
# New


class ListBookView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ListBookSerializer
    queryset = models.Book.objects.all()
    filterset_class = filters.BookFilter


class DeleteBookView(generics.DestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Book.objects.all()
    lookup_field = 'isbn'



class CheckBookView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CheckBookSerializer
    queryset = models.Book.objects.all()
    lookup_field = 'isbn'
