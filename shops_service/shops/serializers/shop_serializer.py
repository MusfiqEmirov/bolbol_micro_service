from rest_framework import serializers

from shops.models.shop import Shop
from shops.models.shop_activity import ShopActivity


__all__ = (
    'ShopSerializer',
    'ShopUpdateSerializer'
)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ShopUpdateSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(
        queryset=ShopActivity.objects.all(),
        many=True
    )

    class Meta:
        model = Shop
        fields = ( 
            "logo",
            "background_image",
            "name",
            "activities",
            "bio",
            "city",
            "address",
            "map_link",
            "shop_working_hours_data"
        )
