from django.db import models


__all__ = [
    'ShopRegistrationRequest',
    ]


class ShopRegistrationRequest(models.Model):
    """Model to store shop registration requests."""
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"

    REGISTRATION_STATUSES = [
        (IN_REVIEW, "In Review"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected")
    ]

    # shop_owner = models.ForeignKey(   ---------There is not user service yet
    #     verbose_name="users.User",
    #     on_delete=models.CASCADE,
    #     related_name="shop_requests",
    #     related_query_name="shop_request",
    #     null=True,
    #     blank=True
    # )
    shop_owner_full_name = models.CharField(
        verbose_name="Shop Owner Full Name",
        max_length=255,
        null=True,
        blank=True
    )
    shop_name = models.CharField(
        verbose_name="Shop Name",
        max_length=255,   
        null=True,
        blank=True
    )
    shop_activities = models.ManyToManyField(
        "shops.ShopActivity", 
        verbose_name="Shop Activities"
    )

    status = models.CharField(
        verbose_name="Status",
        max_length=10,
        choices=REGISTRATION_STATUSES,
        default=IN_REVIEW
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Shop Registration Request"
        verbose_name_plural = "Shop Registration Requests"

    def __str__(self):
        return f"{self.shop_name}"
    
    # def save(self, *args, **kwargs):
    #     # print(1, self.shop_activities)   ------There is not user service yet
    #     if self.status == self.APPROVED:
    #         from shops.models import Shop
    #         if not Shop.objects.filter(owner=self.shop_owner, is_active=True):
    #             shop = Shop.objects.create(
    #                 owner=self.shop_owner,
    #                 name=self.shop_name,
    #             )
    #             print(self.shop_activities)
    #             shop.activities.set(self.shop_activities.all())
    #     return super().save(*args, **kwargs)