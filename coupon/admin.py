from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'use_from', 'use_to', 'amount', 'active']
    list_filter = ['active', 'use_from', 'use_to']
    search_fields = ['code']