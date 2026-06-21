from django.contrib import admin
from .models import Category, Product, Supplier, Customer, StockTransaction, Sale, SaleItem, AuditLog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','sku', 'category', 'supplier', 'cost_price', 'selling_price', 'reorder_level')
    search_fields = ('name', 'sku', 'category__name', 'supplier__name')
    list_filter = ('supplier__name', 'category__name')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name',)

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'transaction_type', 'quantity', 'supplier', 'customer', 'created_by')
    search_fields = ('product__name', 'supplier__name', 'customer__name', 'created_by')
    list_filter = ('supplier__name', 'customer__name', 'transaction_type', 'created_by')
    ordering = ('-created_at',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'created_by')
    search_fields = ('customer', 'created_by',)
    ordering = ('-created_at',)

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'unit_price', 'total_price')
    search_fields = ('product',)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_type', 'model_name', 'object_id', 'timestamp')
    search_fields = ('user', 'model_name')
    list_filter = ('user', 'action_type', 'model_name')
    ordering = ('-timestamp',)