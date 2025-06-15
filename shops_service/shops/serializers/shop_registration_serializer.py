from rest_framework import serializers

from shops.models.shop_registration import ShopRegistrationRequest


__all__ = (
    'ShopRegistrationRequestSerializer'
    )

class ShopRegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopRegistrationRequest
        fields = (
            "shop_owner_full_name",
            "shop_name",
            "shop_activities",
        )
