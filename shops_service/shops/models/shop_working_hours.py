from django.db import models

from .shop import Shop
from utils.constants import TimeIntervals


__all__ = (
    "ShopWorkingHours"
)


class ShopWorkingHours(models.Model):
    shop = models.ForeignKey(
        Shop,
        verbose_name="Shop",
        on_delete=models.CASCADE,
        related_name="working_hours",
        related_query_name="working_hour"
    )
    day_of_week = models.CharField(
        max_length=9, 
        choices=TimeIntervals.WEEKDAYS,
        null=True,
        blank=True
    )
    opening_time = models.TimeField(
        "Opening Time",
        null=True,
        blank=True
    )
    closing_time = models.TimeField(
        "Closing Time",
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ("shop", "day_of_week")

    def __str__(self):
        return f"{self.shop.name} - {self.day_of_week}: {self.opening_time} to {self.closing_time}"
    
