from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(
        _('name'),
        unique=True,
        max_length=150,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('pk',)
