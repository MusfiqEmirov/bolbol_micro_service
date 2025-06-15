from django.contrib import admin

from shops.models.shop_contact import ShopContact


class ShopContactInline(admin.TabularInline):
    model = ShopContact
    extra = 1
    fields = ("phone_number",)
