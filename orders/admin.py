from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'customer',
        'status',
        'total_price',
        'order_date',
    )

    list_filter = (
        'status',
        'order_date',
    )

    search_fields = (
        'customer__username',
        'full_name',
        'phone_number',
    )

    ordering = (
        '-order_date',
    )

    readonly_fields = (
        'order_date',
    )

    inlines = [
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'product',
        'quantity',
        'price',
    )

    search_fields = (
        'product__name',
    )