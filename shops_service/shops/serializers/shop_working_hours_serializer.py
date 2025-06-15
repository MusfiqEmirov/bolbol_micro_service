from rest_framework import serializers

from shops.models.shop_working_hours import ShopWorkingHours


__all__ = [
    'ShopWorkingHoursSerializer'
]


class ShopWorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopWorkingHours
        fields = "__all__"

