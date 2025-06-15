from django.contrib import admin

from shops.models.shop import Shop
from .shop_working_hours_admin import ShopWorkingHoursInline
from .shop_contact_admin import ShopContactInline


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "get_owner_username", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at", "updated_at")
    search_fields = ("name", "owner__username", "address")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "logo", "bio", "background_image")
        }),
        ("Location", {
            "fields": ("address", "map_link", "map_latitude", "map_longitude")
        }),
        ("Owner and Status", {
            "fields": ("owner", "is_active")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )
    inlines = [ShopContactInline, ShopWorkingHoursInline]

    def get_owner_username(self, obj):
        return obj.owner.username if obj.owner else "No Owner"

    get_owner_username.short_description = "Owner"

