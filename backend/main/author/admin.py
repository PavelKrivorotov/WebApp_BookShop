from django.contrib import admin

from . import models


class BookInline(admin.TabularInline):
    model = models.Author.book.through


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

    fields = [
        'name',
    ]

    inlines = [
        BookInline,
    ]
