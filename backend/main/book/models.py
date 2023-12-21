from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    author = models.ManyToManyField(
        'author.Author',
        related_name='book',
    )

    category = models.ManyToManyField(
        'category.Category',
        related_name='book',
    )

    isbn = models.IntegerField(
        _('articl'),
        unique=True,
    )

    image = models.ImageField(
        _('image'),
        blank=True,
    )

    title = models.CharField(
        _('title'),
        max_length=150,
    )

    page = models.IntegerField(
        _('page'),
    )

    state = models.CharField(
        _('state'),
        max_length=7,
        choices=[
            ('PUBLISH', 'PUBLISH'),
            ('MEAP', 'MEAP'),
        ]
    )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('pk',)
