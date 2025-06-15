from django.contrib import admin

from shops.models import ShopActivity

__all__ = (
    'ShopActivityAdmin'
)

@admin.register(ShopActivity)
class ShopActivityAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ("name",)
    list_per_page = 20