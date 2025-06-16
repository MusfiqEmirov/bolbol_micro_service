from django.conf import settings
from django.db import models


__all__ = [
    'Shop',
    ]


class Shop(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Owner',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    # city = models.ForeignKey(
    #     'products.City',
    #     verbose_name='City',
    #     on_delete=models.PROTECT,
    #     related_name='shops',
    #     related_query_name='shop',
    #     null=True,
    #     blank=True
    # )
    # activities = models.ManyToManyField(
    #     'shops.ShopActivity', 
    #     verbose_name='Shop Activities'
    # )
    name = models.CharField(
        'Name',
        max_length=255,
        null=True,
        blank=True
    )
    # slogan = models.CharField(
    #     'Slogan', 
    #     max_length=255, 
    #     null=True, 
    #     blank=True
    # )
    logo = models.ImageField(
        verbose_name='Logo',
        max_length=255,
        upload_to='shops/logos/%Y/%m/%d',
        null=True,
        blank=True
    )
    address = models.TextField(
        verbose_name='Address',
        max_length=255,
        null=True, 
        blank=True
    )
    bio = models.TextField(
        verbose_name='Intro text',
        null=True,
        blank=True
    )
    background_image = models.ImageField(
        verbose_name='Background image',
        upload_to='shops/background/%Y/%m/%d',
        null=True,
        blank=True
    )
    map_link = models.URLField(
        verbose_name='Map location link',
        max_length=255,
        null=True, 
        blank=True
    )
    map_latitude = models.FloatField(
        verbose_name='Map location latitude', 
        null=True, 
        blank=True
    )
    map_longitude = models.FloatField(
        verbose_name='Map location longitude', 
        null=True, 
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Is active', 
        default=True
    )
    created_at = models.DateTimeField(
        verbose_name='Created at', 
        auto_now_add=True, 
        db_index=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at', 
        auto_now=True
    )
    shop_working_hours_data = models.JSONField(
        default=dict,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return f'{self.name}'
