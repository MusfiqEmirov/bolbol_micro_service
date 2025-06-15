from rest_framework import serializers

from shops.models.shop_activity import ShopActivity


class ShopActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopActivity
        fields = (
            "id", 
            "name"
        )
