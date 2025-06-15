from django.contrib import admin

from shops.models.shop_working_hours import ShopWorkingHours


class ShopWorkingHoursInline(admin.TabularInline):
    model = ShopWorkingHours
    extra = 1
    fields = ("day_of_week", "opening_time", "closing_time")