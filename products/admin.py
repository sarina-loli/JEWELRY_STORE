from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
    )

    search_fields = (
        'name',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price',
        'stock_quantity',
        'available',
        'created_at',
    )

    list_filter = (
        'category',
        'available',
    )

    search_fields = (
        'name',
        'description',
    )

    ordering = (
        'name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }