from rest_framework import serializers

from shops.models.shop_contact import ShopContact


__all__ = (
    'ShopContactSerializer'
)


class ShopContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopContact
        fields = "__all__"

