from django.contrib import admin

from . import models


class BookInline(admin.TabularInline):
    model = models.Category.book.through


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

    fields = [
        'title'
    ]

    inlines = [
        BookInline,
    ]
