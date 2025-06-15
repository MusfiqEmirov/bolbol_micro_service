from django.db import models

from .shop import Shop
from utils.validators import validate_phone_number


__all__ = (
    'ShopContact',
)


class ShopContact(models.Model):
    shop = models.ForeignKey(
        Shop,
        verbose_name='Shop',
        on_delete=models.CASCADE,
        related_name='contacts',
        related_query_name='contact',
    )
    phone_number = models.CharField(
        'Phone number', 
        max_length=255, 
        validators=[validate_phone_number],
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Shop contact'
        verbose_name_plural = 'Shop contacts'

    def __str__(self):
        return f'{self.phone_number}'
