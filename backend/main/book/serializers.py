from rest_framework import serializers

from . import models


class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = [
            'isbn',
            'image',
            'title',
            'page',
            'state',
            'author',
            'category',
        ]


class SetBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = [
            'image',
            'title',
            'page',
            'state',
            'author',
            'category',
        ]


class ListBookSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name',
    # )

    # category = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title',
    # )

    class Meta:
        model = models.Book
        fields = [
            'id',
            'isbn',
            'image',
            'title',
            'page',
            'state',
            'author',
            'category',
        ]

class CheckBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['isbn']
