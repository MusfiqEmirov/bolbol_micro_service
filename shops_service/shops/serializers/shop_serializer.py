from rest_framework import serializers

from shops.models.shop import Shop


__all__ = [
    'ShopSerializer'
]


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

