from django.contrib import admin
from . import models




class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', '__str__','is_paid')
    list_filter = ('is_paid',)
    inlines = (OrderItemAdmin,)


@admin.register(models.DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'quantity')
