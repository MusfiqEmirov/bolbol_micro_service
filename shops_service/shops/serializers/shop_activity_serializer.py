from rest_framework import serializers

from shops_service.shops.models.shop_activity import ShopActivity


__all__ = [
    'ShopActivitySerializer',
    ]


class ShopActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopActivity
        fields = (
            "id", 
            "name"
        )
