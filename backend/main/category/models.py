from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(
        _('title'),
        unique=True,
        max_length=150,
    )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('pk',)
