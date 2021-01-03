from django.contrib import admin

from .models import Customer, Address


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name',
                    'last_name', 'customer_id',
                    'created_at', 'currency', 'id']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'address', 'city',
                    'state', 'country',
                    'zip_code', 'id']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)
