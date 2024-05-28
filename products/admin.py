from django.contrib import admin
from .models import Product, Category, Outfit

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class OutfitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
    )


admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
