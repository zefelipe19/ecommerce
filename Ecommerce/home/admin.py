from django.contrib import admin

from .models import Item, ItemOrder


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('id', 'name', 'price', 'promotional_price', 'is_promo')
    list_display_links = ('id', 'name')
    list_editable = ('promotional_price', 'is_promo')


class ItemOrderAdmin(admin.ModelAdmin):
    model = ItemOrder
    list_display = ('id', 'item', 'quantity', 'total_price')


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemOrder, ItemOrderAdmin)
