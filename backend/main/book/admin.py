from django.contrib import admin

from . import models


class AuthorInline(admin.TabularInline):
    model = models.Book.author.through


class CategoryInline(admin.TabularInline):
    model = models.Book.category.through


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'isbn',
        'title',
        'state',
        'page',
    ]

    fields = [
        'isbn',
        'title',
        'image',
        'state',
        'page',
    ]

    inlines = [
        AuthorInline,
        CategoryInline,
    ]
