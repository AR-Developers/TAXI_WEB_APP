from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account, VendorAccount, Profile

class AccountAdmin(UserAdmin):
    # fields = ['first_name', 'last_name']
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff',)
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    filter_vertical = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(VendorAccount)
admin.site.register(Profile)