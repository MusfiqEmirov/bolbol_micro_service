from django.db import models


__all__ = [
    'ShopActivity',
    ]


class ShopActivity(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=64,
        unique=True,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name="Is active",
        default=True
    )

    class Meta:
        verbose_name = "Shop Activity"
        verbose_name_plural = "Shop Activities"

    def __str__(self):
        return self.name