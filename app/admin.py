from django.contrib import admin

from .models import Deals, Customer

class DealsAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'total', 'quantity', 'date')
    list_display_links = ('customer', 'item')
    
admin.site.register(Deals, DealsAdmin)
admin.site.register(Customer)