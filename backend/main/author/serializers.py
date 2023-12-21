from rest_framework import serializers

from . import models


class AddAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = [
            'name',
        ]


class ListAuthorSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title',
    )

    class Meta:
        model = models.Author
        fields = [
            'id',
            'name',
            'book',
        ]
