from django.contrib import admin

from .models import Reservation
from .models import ProductOption
from .models import Book
# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_option', 'email', 'phone', 'status', 'transaction_id', 'created_at', 'completed_at']
    exclude = ['updated_at', 'created_at', 'completed_at', 'product', 'transaction_id', 'payer_id', 'terms', 'status', 'amount']

    def get_readonly_fields(self, request, obj=None):
            if obj: # editing an existing object
                return self.readonly_fields + ('product_option',)
            return self.readonly_fields

    def has_add_permission(self, request):
        return False

class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ['_get_option', 'available', 'reserved', 'purchased', 'updated_at']
    exclude = ['updated_at', 'created_at']
    def has_add_permission(self, request):
        return False
    def get_readonly_fields(self, request, obj=None):
            if obj: # editing an existing object
                return self.readonly_fields + ('product',)
            return self.readonly_fields

class BookAdmin(admin.ModelAdmin):
    pass


# REGISTRY
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Book, BookAdmin)
admin.site.site_header = 'iStackHoldings CRM'

