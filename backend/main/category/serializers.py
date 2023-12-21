from rest_framework import serializers

from . import models


class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            'title',
        ]


class ListCategorySerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title',
    )

    class Meta:
        model = models.Category
        fields = [
            'id',
            'title',
            'book',
        ]
